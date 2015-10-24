import tushare as ts
#ts.get_hist_data('600848')
#
df = ts.get_hist_data('000875');
df.to_csv('E:/day/000875.csv',columns=['open','high','low','close'])
#df.to_json('E:/day/000875.json',orient='records')

print df.get('close', None)[0];
