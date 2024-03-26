# loads the necessary libraries
import quandl
import matplotlib.pyplot as plt

# creates a data frame containing TGT stock data
tgt = quandl.get('WIKI/TGT')

# title
plt.title('Target (TGT) closing stock prices', fontsize=20)

# x and y axis labels
plt.xlabel('Year');
plt.ylabel('Stock price (USD)');

# plot
plt.plot(tgt.index, tgt['Adj. Close'])

# saves the image
plt.savefig("tgtstocklinechart.png")

'''
One of the most useful libraries that includes a multitude of economic data such as stock prices, futures, and unemployment rates is quandl. The quandl library allows users to preprocess, subset, and change the format of data frames, using a much more convenient syntax than pandas, and is especially suited for time series analysis. To use quandl, the library needs to be downloaded and installed by running pip install quandl from the command line.

For more information about the quandl library and specific methods, see the documentation.

The code below creates a line chart for the closing stock prices of Target (TGT) since 1983.