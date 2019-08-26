from webapp.campaign.models import Campaign, Customer


def get_all_campaigns():
    return Campaign.all()


def get_campaign(campaign_id):
    return Campaign.one(campaign_id)


def add_customer_as_propsect(campaign_id, customer_id):
    campaign = Campaign.one(campaign_id)
    customer = Customer.one(customer_id)
    campaign.add_prospect(customer)


def close_sale(campaign_id, customer_id):
    campaign = Campaign.one(campaign_id)
    customer = Customer.one(customer_id)
    campaign.close_sale(customer)

def drop_sale(campaign_id, customer_id):
    campaign = Campaign.one(campaign_id)
    customer = Customer.one(customer_id)
    campaign.drop_sale(customer)
