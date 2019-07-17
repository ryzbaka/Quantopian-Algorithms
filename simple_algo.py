def initialize(context):
    context.security_list=[sid(24),sid(5061),sid(3766)]
    context.xon=sid(8347)
    context.message='Market is now open.'
    schedule_function(open_position,date_rules.every_day(),time_rules.market_open())
    schedule_function(close_position,date_rules.every_day(),time_rules.market_close(minutes=30))
def before_trading_start(context,data):
    print(context.message)

def open_position(context,data):
    print('open')
    print(get_datetime('US/Eastern'))
    for sec in context.security_list:
        order_target_percent(sec,0.25)
def close_position(context,data):
    print('close')
    print(get_datetime('US/Eastern'))
    for sec in context.security_list:
        order_target_percent(sec,0)
    values=data.current(context.security_list,['high','low'])
    print("Today's lows")
    print(values['low'])
    print("Today's highs")
    print(values['high'])
def handle_data(context,data):
    if data.can_trade(context.xon):
        order_target_percent(context.xon,0.20)
