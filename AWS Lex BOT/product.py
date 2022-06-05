import datetime
import pandas as pd
from datetime import date,datetime

productUrl = 'https://myproductdata.s3.amazonaws.com/products.csv'

productPriceUrl = 'https://myproductdata.s3.amazonaws.com/product_prices.csv'
class Product():
    def __init__(self, code, type, resort,name, description,location,price):
        self.code = code
        self.type = type
        self.resort = resort
        self.name = name
        self.description = description
        self.location = location
        self.price = price

    
    def __eq__(self, other):
        return (self.code == other.code)

    def __repr__(self):
        return '<Product ({!r}, {!r},{!r}, {!r}, {!r},{!r},{!r})>'.format(
            self.code, self.type, self.resort, self.name, self.description,self.location, self.price
        )
    def __hash__(self):
      return hash((self.code, self.code))

class ProductService():

    def __init__(self, productUrl, productPriceUrl):
        self.product_data= pd.read_csv(productUrl)
        self.price_data= pd.read_csv(productPriceUrl)

    def getResortByLocation(self, location='Orlando'):
        product_df = self.product_data[self.product_data.Location==location]
        print(type(product_df['Resort'].unique()))
        print(product_df['Resort'].unique())
        return product_df['Resort'].unique()

    def getProductByLocationAndResort(self, departureDatetime, resort, location='Orlando'):
        product_df = self.product_data[(self.product_data.Location==location) & (self.product_data.Resort==resort)].sample(4)
        product_list = []
        print(type(product_df))
        for index, row in product_df.iterrows():
            price = self.getPriceByProduct(row['Product Code'],departureDatetime)
            product_list.append(Product(row['Product Code'],row['Product Type'],row['Resort'],row['Product Name'],row['Product Description'],row['Location'],price))
        return product_list

 
    def getProductByLocation(self, departureDatetime, location='Orlando'):
        product_df = self.product_data[self.product_data.Location==location].sample(3)
        product_list = []
        print(type(product_df))
        for index, row in product_df.iterrows():
            price = self.getPriceByProduct(row['Product Code'],departureDatetime)
            product_list.append(Product(row['Product Code'],row['Product Type'],row['Resort'],row['Product Name'],row['Product Description'],row['Location'],price))
        return product_list

    def getProductByCode(self, productCode, location,departureDatetime):
        filter = (self.product_data['Product Code'].eq(productCode)) & (self.product_data['Location'].eq(location))
        product_df = self.product_data[filter]
        
        product = None
        
        for index, row in product_df.iterrows():
            price = self.getPriceByProduct(row['Product Code'],departureDatetime)
            product = Product(row['Product Code'],row['Product Type'],row['Resort'],row['Product Name'],row['Product Description'],row['Location'],price)
        return product
    
    def getPriceByProduct(self, productCode, departureDatetime):
        self.price_data['Date']= pd.to_datetime(self.price_data['Date'])
        
        filter = (self.price_data['Product Code'].eq(productCode)) & (self.price_data['Date'].le(departureDatetime))
        filter_price_data = self.price_data[filter]
        total_records = filter_price_data.shape[0]
        price =0
        if total_records > 0:
            price = filter_price_data.sort_values("Date")['Price'].head(1).values[0]
        
        return price



productService = ProductService(productUrl,productPriceUrl)
list = productService.getProductByCode(1247,'Orlando',datetime(2022,1,1))
print(list)


print(productService.getResortByLocation())
print(productService.getProductByLocationAndResort(datetime(2022,1,1),'Jungle Book Resort','Orlando'))



#price_data.index.get_loc(date(2016,2,2))



