from decimal import Decimal


def additional_context(fire_area):
    def get_percentage(area):
        result =  (fire_area / area) * 100
        return Decimal(str(result)).quantize(Decimal("0.01")) # Decimal is required because Python doesn't handle floating points very well by default.
    
    def get_times(area):
        result = fire_area / area
        return Decimal(str(result)).quantize(Decimal("0.01"))
    
    rounded_fire_area = Decimal(str(fire_area)).quantize(Decimal("0.01"))
    MELBOURNE_AREA = 9993
    PORT_JACKSON_BAY_AREA = 55
    MURRAY_DARLING_BASIN_AREA = 1059000
    ACT_AREA = 2400

    context_string = f"""
        In this hypothetical scenario, `{rounded_fire_area}` square kilometres of fire would be burning simultaneously across the entire country. 🤯
        
        ### Other things this fire compares to:
        - `{get_percentage(MELBOURNE_AREA)}%` of Greater Melbourne. 😧
        - `{get_times(PORT_JACKSON_BAY_AREA)}` Port Jackson Bays 🌊
        - `{get_percentage(MURRAY_DARLING_BASIN_AREA)}%` of the Murray-Darling Basin. 🌾
        - `{get_percentage(ACT_AREA)}%` of the ACT. 🏙️
        """

    return context_string