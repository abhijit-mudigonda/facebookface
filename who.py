import subprocess
import os
import requests
import facebook

def main():

            subprocess.call(["fswebcam", "user_photo.jpg"])
            
            cfg = {
                "page_id" : "100001816035196",
                "access_token" : "EAACEdEose0cBAISqMl4CEEyRNSZC9cSKeN5ztVdZBz8ymhoJOZClloqtZAxdXXW7u3TI6oy7YOIV5ftzE3q33Hym3YllW651YxqIOJNaNLVDNJW0ZCqT0sqVeokg55gZBgGRdZCD43kDkreNZCqb8StYYdbZCZB6aNaxamahy5SR9UEgZDZD"
                }

            api = get_api(cfg)
            status = api.put_photo(image=open('user_photo.jpg','rb'))
            posts = api.get_connections(id='me', connection_names='posts')
            print posts
def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    return graph

if __name__ == "__main__":
    main()
            
            #set up user ID thing based on the stackexchange
            
            #submit a facebook post request to privately post 
            #the photo
            
            #somehow access the "suggested tags" from facebook and 
            #do things - maybe play around with all the information
            #you can extract from a photo? 

            

