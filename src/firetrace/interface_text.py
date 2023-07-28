q_and_a = """        
        ### **Q: What's the deal with Firetrace? 🔍**\n
        A: Picture this—it's like having your very own bushfire fortune teller! 
        🔮 Firetrace is an AI-powered web interface that predicts the severity of bushfire events all across Australia. 
        🌍 It's armed with projected weather data, BOM weather observatories and NASA's MODIS satellite intel. 
        It even considers time information to get climate change trends. 🦸‍♂️🔥
        \n

        ### **Q: What is the inspiration behind Firetrace?** 🤔 \n
        A: Those bushfires! They cause habitat loss, put many animal species at risk, and drastically impact the economy 😢📉 
        The series of bushfires that took place in Australia is a clear demonstration of this. 
        ☝️ So, we put our heads together to conjure up Firetrace—a cutting-edge tool that helps us predict the severity of these fiery events.
        This will be helpful in making smarter decisions and being prepared to take on the bushfire challenges head-on! 💪🌳
        \n

        ### **Q: How do I use Firetrace?** 🎉 \n
        A: It's easy-peasy! 🔥 
        Simply enter in values for the input boxes below, and you'll unlock access to the hottest predictions, 
        and uncover the secrets of bushfire severity. 
        The prediction you receive will be the number of square kilometres of land the fire covers that day.
        (Keep in mind that it's not completely right, we're not wizards here 🧙  - but it does have reasonable accuracy)
        \n

        Let's work together to face these fiery challenges to create a safer future! 🚀🌿
        """

def additional_context(scan_area):
    def get_percentage(scan_area, area):
        return round((scan_area / area) * 100, 2)
    
    def get_times(scan_area, area):
        return round(scan_area / area, 2)
    
    LARGEST_EVENT = 5854.7
    MELBOURNE_AREA = 9993
    PORT_JACKSON_BAY_AREA = 55
    MURRAY_DARLING_BASIN_AREA = 1059000
    ACT_AREA = 2400

    context_string = f"""
        The predicted area of your fires 🤓 was `{round(scan_area, 2)}` square kilometres. 🤯 This is `{get_percentage(scan_area, LARGEST_EVENT)}%` of the largest fire event 🔥 in our database, at {round(LARGEST_EVENT, 2)} square kilometres, recorded on the 19th of September 2011.
        
        ### Other things this fire compares to:
        - `{get_percentage(scan_area, MELBOURNE_AREA)}%` of Greater Melbourne. 😧
        - `{get_times(scan_area, PORT_JACKSON_BAY_AREA)}` Port Jackson Bays 🌊
        - `{get_percentage(scan_area, MURRAY_DARLING_BASIN_AREA)}%` of the Murray-Darling Basin. 🌾
        - `{get_percentage(scan_area, ACT_AREA)}%` of the ACT. 🏙️
        """

    return context_string