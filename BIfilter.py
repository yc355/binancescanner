def filter(configs=None, vol=None, price=None, btc_price=None):
    if configs['DAILY_VOLUME']:
        if not (configs['DAILY_VOLUME_MIN'] <= vol <= configs['DAILY_VOLUME_MAX']):
            return False
    
    if configs['DAILY_DOLLAR_VOLUME']:
        if not (configs['DAILY_DOLLAR_VOLUME_MIN'] <= vol * btc_price <= configs['DAILY_DOLLAR_VOLUME_MAX']):
            return False

    return True
