# bulk-instance-lock
This is a simple Python script that allows you to bulk enable the 'Lock' (Provisioning > Instances > Actions > Lock) feature on instances in Morpheus. 


**How it works:**
1. Send an API call to get all instances - https://apidocs.morpheusdata.com/reference/listinstances
2. Filter through the response, collect all the instance IDs and save them in an array
3. Iterate through the values in the array and append them to the URL for the API call to lock an instance - https://apidocs.morpheusdata.com/reference/lockinstance

I created this to answer a question in this forum post: 
- https://discuss.morpheusdata.com/t/unable-to-remove-server-that-still-has-locked-instances-on-it/1260/4


