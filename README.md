# bulk-instance-lock
This is a simple Python script that allows you to bulk enable the 'Lock' (Provisioning > Instances > Actions > Lock) feature on instances in Morpheus. 


**How it works:**
1. Send an API call to get all instances - https://apidocs.morpheusdata.com/reference/listinstances
2. Filter through the response, collect all the instance IDs and save them in an array
3. Iterate through the values in the array and append them to the URL for the API call to lock an instance - https://apidocs.morpheusdata.com/reference/lockinstance

I created this to answer a question in this forum post: 
- https://discuss.morpheusdata.com/t/unable-to-remove-server-that-still-has-locked-instances-on-it/1260/4


**Tips/Advice:**
- [Update the maximum number of instances to return](https://apidocs.morpheusdata.com/reference/listinstances#:~:text=QUERY%20PARAMS-,max,-int64) in the script
- It may be best to perform this request in batches of ~50 instances. I have only tested it on my appliance with 5 instances. I'm not sure what the impact would be of sending a request to update the lock status on 100s of instances (whether the app node can handle that is something that needs to be tested).
- Update the appliance URL and API token to point to your appliance 


Covered under the [Morpheus Open Source Code Policy](https://support.morpheusdata.com/s/article/Morpheus-Open-Source-Code-Support-Policy?language=en_US)
