import json
#comment
class Premiua:
    def __init__(self, table_name, canonical_marketplace_id, gl_product_group_name, fma_version, price_range_coefficient_list):
        self.table_name = table_name
        self.canonical_marketplace_id = canonical_marketplace_id
        self.gl_product_group_name = gl_product_group_name
        self.fma_version = fma_version
        self.price_range_coefficient_list = price_range_coefficient_list

class CoefficientList:
    def __init__(self, asp_range_start, asp_range_end, coefficient_list):
        self.asp_range_start = asp_range_start
        self.asp_range_end = asp_range_end
        self.coefficient_list = coefficient_list

coe_1 = CoefficientList(0, 4.610000133514404296875, {'fast_track_premium_a':0e0, 'fast_track_premium_b':0e0})
coe_2 = CoefficientList(0, 4.63000011444091796875, {'fast_track_premium_a_prime':0e0, 'fast_track_premium_b_prime':0e0})
#print vars(coe_1)
#print json.dumps(vars(coe_1),sort_keys=True, indent=4)
#print json.dumps(vars(coe_2),sort_keys=True, indent=4)

gl_book = Premiua('fma_version_configs', "3", 'gl_book', "DEFAULT", [vars(coe_1), vars(coe_2)])

#print vars(gl_book)
#print json.dumps(vars(gl_book),sort_keys=True, indent=4)
