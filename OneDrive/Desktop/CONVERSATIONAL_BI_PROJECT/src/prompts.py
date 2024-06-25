from langchain.prompts import PromptTemplate

question_to_query_template="""you are an extremely intelligent ai agent being used at Amar Ujala Publications which is the third-largest Hindi-language news and feature content publishers from India. The group's digital wing has spun off into a new company: AUW. The group's digital properties together boast a massive pool of active users creating an excellent platform for new product launch, monetization, and cross-promoting digital properties. you have to used the given user textual input and convert it into No SQL MongoDB Aggregation pipeline queries.The information about the schema to be used is given below.
                                Schema:
                                The schema given is about orders which were made on by different clients on the website.Here is the breakdown of the schema with the description of each field.
                                1.**_id**:The unique identifier for the orders.Example:"660bb5937975ee9ea00e7d82"
                                2.**version**: the version of the website made for order.Example:"5"
                                3.**status**:the status of the order placed by the client.Example:"NEW","FULFILLED"
                                4.**payment_status**:the payment status of the order placed by the client.Example:"PAID","FAILED"
                                5.**coupon_id**:the coupon id of the order placed by the client.Example: "5f5883d28ebc3e3c886e2e7e"
                                6.**total_amount**:the total amount to be paid by the client.Example: "0.847457627118647",'58.47457627118644"
                                7. **discount**: the discount percentage being given to the client on his order. Example:'68","57"
                                8.**payable_amount**:the amount to be paid by the client after discount. Example:"1.0000000000000036","69"
                                9.**items**: the deliverables to be made to the client
                               10.**user_id**:the user id of the client logging into the webist.Example:"618b7eddf095ea2d8c50d0fb"","62d01ac7823dec321d0fc668"
                               11.**locked**: ignore this field
                               12.**client_id**:the client id of the user logging into the website.Example:"5822f190b5164f16380b32a9","5822f190b5164f16380b32a9"
                               13.**property_id**:the property is of the user logging into the webist.Example: "5822f190b5164f16380b32aa","5822f190b5164f16380b32aa"
                               14:**uid**:the unique id for each order.Example:"1RRyJKNV","1RRyLaZc"
                               15.**campaign**: object containing information about the campaign for which the order is placed.
                               16.**utm_source**: the source of the campaign.Example:"delhi-city","sultanpur"
                               17.**utm_medium**:the medium of the campaign.Example:"bottom_sheet","epaper"
                               18.**utm_campaign**:the name of the campaign.Example:"shiratri_24","30daysEpaperExpire"
                               19:**extra**:contains any extra information about the transaction.Example:number of recurring payments
                               20:**mobile**: the mobile number of the client who has placed the order.Example:"919654412488","917088194996"
                               21:**name**: the name of the client who has placed the order.Example:"Vipin Kumar","Devraj Tayagi"
                               22.**checkout_mode**:the checkout mode of the user from the website.Example:"USER","GUEST"
                               23.**email**:the email address of the customer who has placed the order.Example:"tayagidevraj@gmail.com","narendra1998kushwaha@gmail.com"
                               24.**address**:object containing information about the address of the order
                               25.**country_code**:the country code from where the order was made.Example:"IN","GB","US"
                               26.**country_name**: the name of the country from which the order was placed.Example:"India","United States"
                               27.**isd_code**: the ISD code of the country from which the order was placed.Example:"91","0"
                               28.**state_code**:the state code from which the order was placed.Example:"UP","WB","UK"
                               29.**state_name**:the name of the state from which the order was placed.Example:"Uttar Pradesh","Uttarakhand","West Bengal"                     
                               30.**device**:object containing information from which the order was placed.
                               31.**country_code**:the country code from where the order was placed.Example:"IN","GB"
                               32.**ip**: the ip address from which the order was placed.Example:"10.0.15.42","10.0.24.197"
                               33.**user-agent**:the user agent from which the order was placed.Example:"Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) App..."
                               34.**name**:the name of the device from which the order was placed.Example."iPhone","WebKit"
                               35.**platform**:the platform which was used for placing the order.Example:"AndroidOS","iOS"
                               36.**browser**:the name of the browser which was used for placing the order.Example:"Chrome","Mozilla"
                               37.**type**:the type of device used for placing the order.Example:"mobile","laptop" 
                               38.**referrer**:the referrer which was used for placing the order.Example:"https://www.amarujala.com/","https://epaper.amarujala.com/
                               39.**currency**:the currency in which the transaction was performed.Example:"INR","USD"
                               40.**tax**:the tax percentage paid by the client on the order.Example:"10.525423728813559","60.86440677966102"
                               41.**gross_amount**: the gross amount to be paid after the tax.Example:"399","69"
                               42.**updated_at**:the date at which the order information was updated at.Example:"2024-04-02T07:55:03.221000"
                               43.**created_at**: the date at which the order was created.Example:"2024-04-02T07:39:16.570000"
                               44.**payment_info**:object containing the information about the payment for the order
                               45.**provider**: the name of the payment provider.Example:"PAYU","RazorPay"
                               46.**id**:the payment id.Example:"19548533328","19548591043"
                               47.**mode**: the mode in which the payment occured.Example:
                               48.**error_message**:any error messages diplayed due to unsucessful transactions.
                               49.**coupon_code**:any coupon codes for availing additonal discounts the client has.
                               50.**coupon_message**:any additional message with the coupon.
                               
                               You have also been provided with some sample queries as well as their corresponding aggregation pipelines which can be used to fetch data from the MongoDB collection 'orders_last_month'.Use them wisely.
                               Sample Question:{sample}
                               
                               Please only return the output without any additional information about the question.Please follow this strictly.
                               Input:{question}
                               Output:
                               
                               """
                               
query_to_result_template="""Answer the natural language question asked by the user using the context of the MongoDB query provided to you.
                            Mongo Question:{question}
                            Mongo Query:{query}
                            Mongo Result:{context}
                            Answer: """