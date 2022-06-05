FROM amazon/aws-lambda-python
ADD product.py /
ADD ProductBot.py /
RUN pip install numpy
RUN pip install pandas
RUN pip install awslambdaric
CMD ["ProductBot.lambda_handler"]