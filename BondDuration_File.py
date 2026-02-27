import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
    m_eff = m * ppy
    coupon = face * couponRate / ppy
    i = np.arange(1, m_eff + 1)
    discount = 1 / (1 + y / ppy) ** i
    cf = np.full(m_eff, coupon)
    cf[-1] += face
    pvcf = cf * discount
    price = np.sum(pvcf)
    duration = np.sum(i * pvcf) / price
    return(duration / ppy)
  
