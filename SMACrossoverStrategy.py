def initialize(context):
    context.aapl=sid(24)

def handle_data(context,data):
    hist=data.history(context.aapl,'price',50,'1d')
    sma50=hist.mean()#50 day simple moving average
    sma20=hist[-20:].mean()#20 day simple moving average
    #order(security,amount,style=ordertype) here you're ordering amount number of shares
    #ordertype can be MarketOrder,StopOrder,LimitOrder or StopLimitOrder
    #order_value(security,amount,style=ordertype) here you're ordering 'amount' worth of stock
    if sma20>sma50
        order_target_percent(context.aapl,1.0)# we want 100% of our portfolio to be long in apple
    elif sma20<sma50:
        order_target_percent(context.aapl,-1.0)
        
