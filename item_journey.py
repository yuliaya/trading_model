from Lifetime.predict_lifetime import predict_lifetime
from Predict_price.future_price import future_price
from Predict_price.transactional_pricing import transactional_pricing
from Decision_making.decision import check_invest_interest, user_decision, check_if_worth_selling
from Decision_making.market_engine import trading_algo

ROUTE = {  # this dict defines the next state of any item while considering the current one
    'start': predict_lifetime,
    'predict_lifetime': future_price,
    'future_price': check_invest_interest,
    'transactional_pricing': transactional_pricing,
    'user_decision': user_decision,
    'user_selling_decision': check_if_worth_selling,
    'trading': trading_algo,
}