from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Swagger API!"}


@app.get('/mobilebatch/test')
async def get_mobilebatch_test():
    example_data = {
        "product":{
            "product_name": "Mozzarella cheese",
            "product_description":"Our state-of-the-art technology, which has been designed specifically for our plant and production requirements, has been sourced predominately from Italy and is only one of three plants of this kind in the world.The steam injected technology uses a continuous process along the line which ensures the moisture content and protein structure of the block is retained to maintain superior texture, structure and functionality.",
            "product_barcode":"Product Barcode",
            "product_unit_weight":"Product Unit Weight",
            "product_dimension":"Product Dimension",
            "product_image":"https://oziris.azurewebsites.net/trace/getimg/images/beston/mozzarellacheese/cheese.png",
            "product_image_2":"https://oziris.azurewebsites.net/trace/getimg/images/beston/mozzarellacheese/aboutproduct.png",
            "product_image_3":"https://oziris.azurewebsites.net/trace/getimg/images/beston/mozzarellacheese/ingredient.png",
            "product_character":["New state-of-the-art technology delivering product of the highest quality.",
                                "Made from milk locally sourced in South Australia.",
                                "Low oiling and improved stretch.",
                                "Firm and fibrous in texture for high volume shredding.",
                                "Even browning at higher temperatures.",
                                "Made by experienced cheesemakers who balance the use of modern equipment with traditional artisan methods."
                                ],
            "product_link":"https://www.youtube.com/watch?v=zPenGq4XOXU",
            "product_nutrition_info":{
                "info":[
                    {"nutrition_name":"Energy(Kj)","per_serving":"318(Kj)","per_100g":"1270(Kj)"},
                    {"nutrition_name":"(cal)","per_serving":"76(cal)","per_100g":"304(cal)"},
                    {"nutrition_name":"Protein(g)","per_serving":"6.4(g)","per_100g":"25.4(g)"},
                    {"nutrition_name":"Tat,total(g)","per_serving":"5.4(g)","per_100g":"21.4(g)"},
                    {"nutrition_name":"-saturated(g)","per_serving":"4.0(g)","per_100g":"16.2(g)"},
                    {"nutrition_name":"Carbohydrates(g)","per_serving":"< 1(g)","per_100g":"< 1(g)"},
                    {"nutrition_name":"-sugars(g)","per_serving":"< 1(g)","per_100g":"< 1(g)"},
                    {"nutrition_name":"Sodlum(mg)","per_serving":"138(mg)","per_100g":"550(mg)"},
                    {"nutrition_name":"Calclum(mg)","per_serving":"178(mg)","per_100g":"710(mg)"}
                ]
                },
            "product_ingredient_info":{
                "info":[
                    {"ingredient_name":"Pasteurised Milk","ingredient_group":"Dairy"},
                    {"ingredient_name":"Salt","ingredient_group":"Nutrients"},
                    {"ingredient_name":"Enzymes(Non Animal Rennet)","ingredient_group":"Enzymes"},
                    {"ingredient_name":"Start Culture","ingredient_group":"Cultures"},
                ]
            }
        },
         "batch":{
            "batch_number":"1234567",
            "serial_number":"1100001",
            "sscc":"SSCC",
            "manufacture_date":"10/03/2023",
            "manufacture_time":"Manufacture Time",
            "best_before_date":"Best Before Date",
            "expiration_date":"Expiration Date",
            "weight":"Weight",
            "status":"Status",
            "code":"Code",
        },
        "traces":[
            {
                "trace_id":"Trace ID 1",
                "trace_time":"Trace Time",
                "trace_location":"Trace Location",
                "trace_status":"Trace Status",
                "trace_description":"Trace Description",
                "latitude":"37.7749",
                "longitude":"-122.4194",
            },
            {
                "trace_id":"Trace ID 1",
                "trace_time":"Trace Time",
                "trace_location":"Trace Location",
                "trace_status":"Trace Status",
                "trace_description":"Trace Description",
                "latitude":"37.3364",
                "longitude":"-121.8904",
            },
            {
                "trace_id": "Trace ID 1",
                "trace_time": "Trace Time",
                "trace_location": "Trace Location",
                "trace_status": "Trace Status",
                "trace_description": "Trace Description",
                "latitude": "38.5816",
                "longitude": "-121.4944",
            }
        ],
        "brand":{
            "brand_name":"Beston",
            "brand_description":"As the planet grows and emerging economies enjoy a better standard of living, they seek safe and sustainable foods to help them realise their human potential. Beston Global Food Company Limited (BFC) aims to provide natural and verifiably safe food and beverages to global markets so that consumers can make healthy choices. We do this by owning the raw materials, taking advantage of technology in the production process and controlling distribution.",
            "brand_image":"https://oziris.azurewebsites.net/trace/getimg/images/beston/aboutcompany.png",
            "brand_website":"https://bestonglobalfoods.com.au/",
            "phone":"+61 8 8470 6500",
            "email":"admin@bestonglobalfoods.com.au",
            "brand_facebook":"https://www.facebook.com/bestonglobalfoods/",
            "brand_linkedin":"https://www.linkedin.com/company/beston-global-food-company/about/",
            "brand_twitter":"https://twitter.com/bestonglobal/",
            "brand_acn":"© 2019 Beston Global Food Company Ltd ACN 603 023 383"
        }
    }
    return example_data