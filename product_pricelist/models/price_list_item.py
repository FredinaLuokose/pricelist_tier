from odoo import api, fields, models


class PriceListItem(models.Model):
    _inherit = "product.pricelist.item"

    price_tire_ids = fields.One2many(
        "tire.list",
        "price_list_id",
        string="Tires",
    )

    compute_price = fields.Selection(
        selection=[
            ('fixed', "Fixed Price"),
            ('percentage', "Discount"),
            ('formula', "Formula"),
            ('tiered', "Tiered")
        ],
        index=True, default='fixed', required=True
    )

    price_list_product_id = fields.Many2one("product.product", string="Product Variant")

    class TireList(models.Model):
        _name = "tire.list"
        _description = "Tires of price list"

        product_id = fields.Many2one("product.product", string="Product")
        price_list_id = fields.Many2one("product.pricelist.item", string="Price List Item")
        tire_id = fields.Integer(string="Tire ID", required=True)
        tire_quantity_from = fields.Float(string="Tire From", required=True)
        tire_quantity_to = fields.Float(string="Tire To", required=True)
        list_price = fields.Float(string="List Price", required=True)