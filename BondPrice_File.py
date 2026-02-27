import numpy as np
def getBondPrice(y, face, couponRate, m, ppy=1):
    m_eff = m * ppy
    coupon = face * couponRate / ppy
    i = np.arange(1, m_eff + 1)
    discount = 1 / (1 + y / ppy) ** i
    price = np.sum(coupon * discount) + face * discount[-1]
    return(price)
  
