from typing import Optional
import requests
import base64
import json


class HtmlToPdf:
    """This class takes html text as string and converts it into PDF using "doppio" service and returns its url in response,
        it has get_html_string method, set_html_string, get_doppio_api_url_sync, get_doppio_api_url_direct
            get_headers, generate_pdf
        required parameter doppio <api_key> while class initialisation"""
    
    def __init__(self, doppio_api_key : str):
        """Takes doppio_api_key, initializes _doppio_api_key, _encoding, _base64  returns None"""
        # print(doppio_api_key)
        self._doppio_api_key = doppio_api_key
        self._encoding = 'UTF-8'
        self._base64 = "ascii"

    def get_html_string(self) -> str:
        """No parameters, returns html text string"""
        return self._html_string
    
    def set_html_string(self, html_string: str)-> None:
        """No parameters, returns html text string"""
        self._html_string = html_string
    
    def get_doppio_api_url_sync(self) -> str: 
        """No parameters, returns doppio api sync url """
        return "https://api.doppio.sh/v1/render/pdf/sync"
    
    def get_doppio_api_url_direct(self) -> str:
        """No parameters, returns doppio api direct url """
        return "https://api.doppio.sh/v1/render/pdf/direct"
             
    def get_headers(self) -> dict:
        """No parameters, returns headers Authorization and Content-Type in dictionary  """
        return {
            'Authorization': f'Bearer {self._doppio_api_key}',
            'Content-Type': 'application/json'
        }

    def get_image_file_as_base64_data(self, image_path: str) -> str:
        """This function takes image_path as parameter and returns converted base64 image string as base64_string"""
        with open(image_path, 'rb') as f:
            base64_bytes = base64.b64encode(f.read())
            base64_string = base64_bytes.decode("ascii")
            return base64_string
        
    def generate_pdf(self, data: Optional[dict]=None) -> dict:
        """ Taske data as a dictionary as parameter if not passed then it's None,
            returns a dictionary(status, message, pdf-url) of PDF url generated using doppio
        """
        try:
            if data:
                for key, value in data.items():
                    self._html_string = self._html_string.replace(f"{{{key}}}", value)
            HTML = self._html_string.encode(encoding= self._encoding)
            base64_bytes = base64.b64encode(HTML)
            base64_string = base64_bytes.decode(self._base64)
            payload = json.dumps({
                "page": {
                    "pdf": {
                        "printBackground": True,
                        "format": "A4",
                        # "scale": 0.5
                    },
                    "setContent": {
                        "html": base64_string
                    }
                }
            })
            headers = self.get_headers()
            url = self.get_doppio_api_url_sync()
            response = requests.request("POST", url, headers=headers, data=payload)
            response = response.json()
            result ={
                "status": response['renderStatus'],
                "message": "Successfully generated PDF file from HTML.",
                "pdf-url": response['documentUrl']
            }
        except Exception as e:
            result ={
                "status": 400,
                "message": "Bad Request.",
                "pdf-url": None
            }
        return result 
        






	






































# s1.set_html_string("""
#                    <!DOCTYPE html><html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>My Website</title> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">  
#                    <style type="text/css"> img { border-radius: 50%; } .left{ padding:30px; } .main-left{ padding-left:2%; } </style> </head> <body> <main> <div clas="row"> <table style = "width:100%"> 
#                    <tr> <td style="width:50%" class="left"> <img src="http://codeskulptor-demos.commondatastorage.googleapis.com/pang/HfReHl5.jpg" alt="Avatar" style="width:100px; float: left;"> 
#                    </td> <td class="left"> <img src="http://codeskulptor-demos.commondatastorage.googleapis.com/pang/HfReHl5.jpg" alt="Avatar" style="width:100px; float: right;"> 
#                    </td> </tr> </table> <h3 class="main-left"> Your Adequacy and Suitability Check </h3 > <p class="main-left"> Page 3/10</p> <p class="main-left"> Your information</p> <br> <p class="main-left " style="color: green;" >Knowledge & Experiences</p> 
#                    <p class="main-left " style="color: green;">Knowledge</p> <p class="main-left">[Text of Question 1.1]</p> <p class="main-left">Answer</p> <p class="main-left">[Text of Question 1.2]</p> <p class="main-left">Answer</p> <p class="main-left" style="color: green;">Experiences</p>
#                    <p> <span class="main-left">Bonds: ”Yes” / ”Not applicable”</span><br> <span class="main-left">Number: Answer </span> <span class="main-left">Volume: Answer</span> </p> <p> <span class="main-left">Bonds: ”Yes” / ”Not applicable”</span><br> 
#                    <span class="main-left">Number: Answer </span> <span class="main-left">Volume: Answer</span> </p> <p> <span class="main-left">Open investment funds (excluding open real estate funds): ”Yes” = checked / No = ”Not applicable”</span><br> <span class="main-left">Number: Answer </span>
#                    <span class="main-left">Volume: Answer</span> </p> <p> <span class="main-left">Closed-end investment funds or open real estate funds: If checked = ”Yes” / if not checked = ”Not applicable”</span><br> <span class="main-left">Number: Answer </span>
#                    <span class="main-left">Volume: Answer</span> </p> <p> <span class="main-left">Renewable Energy Fund: If checked = ”Yes” / if not checked = ”Not applicable”</span><br> 
#                    <span class="main-left">Number: Answer </span> <span class="main-left">Volume: Answer</span> </p> <span class="main-left" style="color: green;">Risk Tolerance</span>
#                    <br> <span class="main-left">[Description of the risk classification selected]</span> </div> </main> </body> <script> </script></html>
#                    """)
# s1.set_html_string(html_string='<!DOCTYPE html><html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>My Website</title> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script> <style type="text/css"> img { border-radius: 50%; } .left{ padding:20px; } </style> </head> <body> <main> <h1>Welcome to My Website</h1> <div clas="row"> <table style = "width:100%"> <tr> <td style="width:50%" class="left"> <img src="img_avatar.png" alt="Avatar" style="width:100px; float: left;"> </td> <td class="left"> <img src="img_avatar.png" alt="Avatar" style="width:100px; float: right;"> </td> </tr> </table> <h2> Your Adequacy and Suitability Check </h2> </div> </main> </body> <script> </script></html>')
