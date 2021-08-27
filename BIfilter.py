def filter(configs=None, vol=None, price=None, change_pct=None, btc_price=None):
    if configs['DAILY_VOLUME']:
        if not (configs['DAILY_VOLUME_MIN'] <= vol <= configs['DAILY_VOLUME_MAX']):
            return False
    
    if configs['DAILY_DOLLAR_VOLUME']:
        if not (configs['DAILY_DOLLAR_VOLUME_MIN'] <= vol * btc_price <= configs['DAILY_DOLLAR_VOLUME_MAX']):
            return False

    if configs['DOLLAR_PRICE']:
        if not (configs['DOLLAR_PRICE_MIN'] <= price * btc_price <= configs['DOLLAR_PRICE_MAX']):
            return False

    if configs['CHANGE_PCT']:
        if not (configs['CHANGE_PCT_MIN'] <= change_pct <= configs['CHANGE_PCT_MAX']):
            return False

    return True
