
import openai
import requests

def fetch_data_from_api(api_url, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}

def chatbot_response(prompt, api_key):
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=prompt,
          max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def main():
    api_key = 'sk-++'

    # Dictionary mapping API names to their URL and access token
    
    apis = {
        'api1': {'url': 'https://cosylab.iiitd.edu.in/rdbapi/recipeDB/searchRecipeByProtein/195:196.5', 'token': 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI1N1R4M2FWRzR0N0Q5YW00TDlod1VHR2tPVVlvOUpwVFd1VTNmTWxrY1lBIn0.eyJleHAiOjE3MDAyNzIzNDMsImlhdCI6MTcwMDI3MjA0MywianRpIjoiY2EzMmIyMWMtNWUyMC00NGY3LThjZjYtZGU5Zjg3MjNmMWU2IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL2Jvb3RhZG1pbiIsImF1ZCI6WyJhcHAtYWRtaW4iLCJhcHAtdG9kbyIsImFjY291bnQiXSwic3ViIjoiMmEzNzU0NzAtMjU4Ni00MDM4LWEzODUtMTY1OGMxOGVjMTJhIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYXBwLWltcyIsInNlc3Npb25fc3RhdGUiOiI1OGZmZTZmMy1lN2M5LTRkMDktODcwMi04MTNiMzE0YTc1NmEiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhcHAtYWRtaW4iOnsicm9sZXMiOlsiYWRtaW4iXX0sImFwcC10b2RvIjp7InJvbGVzIjpbImFkbWluIiwidXNlciJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZm9ya2l0LWhhY2thdGhvbiJ9.XzhoXaKftvFgi-eixHeZswjhb5pkamXgFCBTuQNxz542eJhHAMI2DvVTpsKsNnktMTqZkZCqvf_RHg5WSYgzDPxjBqk_H0zJgoIISeVugdjk3J6HhAlcfmKe7vKLJsiXmIBnLYupyoHND455bJfrDlQjuVJ8xqrqAwkVjTE_WtUPBl7WLRABA8CnPlW8ESdvKrn_4jAJVFL8mKLJoC8s55PPZ4H8nTYTNupXfJ3rMeT9rcFxuTn9J_oyjQQJUJC_J6oeWBJ8HZypNrpwLsBpzTMzwARDrV_sSiXqKGll6oZMHVGXmu74Cjpq2kqBQRrXUbMVe-VswXprBcJlP38UGg'}, #protein
        'api2': {'url': 'https://cosylab.iiitd.edu.in/rdbapi/recipeDB/searchRecipeByEnergy/195:196.5', 'token': 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI1N1R4M2FWRzR0N0Q5YW00TDlod1VHR2tPVVlvOUpwVFd1VTNmTWxrY1lBIn0.eyJleHAiOjE3MDAyNzI2NzUsImlhdCI6MTcwMDI3MjM3NSwianRpIjoiZjA4MjY2MjctZDcyOC00YmMzLWI5Y2MtN2Q3NmZlOTQyYmI0IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL2Jvb3RhZG1pbiIsImF1ZCI6WyJhcHAtYWRtaW4iLCJhcHAtdG9kbyIsImFjY291bnQiXSwic3ViIjoiMmEzNzU0NzAtMjU4Ni00MDM4LWEzODUtMTY1OGMxOGVjMTJhIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYXBwLWltcyIsInNlc3Npb25fc3RhdGUiOiIxMmNkM2JmNS01MjM1LTRmN2MtYTE4MC04NzUzZWIwZDYyMDEiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhcHAtYWRtaW4iOnsicm9sZXMiOlsiYWRtaW4iXX0sImFwcC10b2RvIjp7InJvbGVzIjpbImFkbWluIiwidXNlciJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZm9ya2l0LWhhY2thdGhvbiJ9.TydibcwHypPnrdI-qye41lROK8LMSeJBZ78gC2ehfczlIYSbVBz3HA2mMUjMWwFiqAhlxhmBxrXSoaxm_vCuNrKN0i98TGSWHeeJDsVLICqqAiXi0M6twxhsvwPUFCdQjdKZY38Lu6MjlLFfurDI1ZbNYzevS0c9C9DfZXfmIRCHZ0rfh92F9qh4ES6QI7VraSnvglJeSzrYhmqBFXP6NbZSljWcF7KZk4RzdIc17vO38LqctMJSirbPAIR7mKNCPXffHw4XkeeO3mY7fXjBie1J4AzguEdOjtnaj5wh9N2Ej9bneRB3YHv6RG1rnmWX6q5Y1SYr-2ZYsRQX-1SJIg'},  #Energy
        'api3': {'url': 'https://cosylab.iiitd.edu.in/rdbapi/recipeDB/searchRecipeByCalorie/195:196.5', 'token': 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI1N1R4M2FWRzR0N0Q5YW00TDlod1VHR2tPVVlvOUpwVFd1VTNmTWxrY1lBIn0.eyJleHAiOjE3MDAyNzMyOTIsImlhdCI6MTcwMDI3Mjk5MiwianRpIjoiZDc1OWNhNjYtMWE3Yi00OWU3LWI1ZDctZjQ3OTBiOGIxNWQ3IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL2F1dGgvcmVhbG1zL2Jvb3RhZG1pbiIsImF1ZCI6WyJhcHAtYWRtaW4iLCJhcHAtdG9kbyIsImFjY291bnQiXSwic3ViIjoiMmEzNzU0NzAtMjU4Ni00MDM4LWEzODUtMTY1OGMxOGVjMTJhIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiYXBwLWltcyIsInNlc3Npb25fc3RhdGUiOiI2NmRjOTJiZC1mZWE5LTQ0MzAtYmU1ZC0wOTJjODZmMDVkMTQiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhcHAtYWRtaW4iOnsicm9sZXMiOlsiYWRtaW4iXX0sImFwcC10b2RvIjp7InJvbGVzIjpbImFkbWluIiwidXNlciJdfSwiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZm9ya2l0LWhhY2thdGhvbiJ9.dl4UzweMJAFIb4-1el4h_Bxo6WqmdYtuBzKr2ck1x_RiWXI3U3o0jsmr0MGNGZ7I88r0gHqXzpJMguMzS-Xu2dmdPV2GtQO81sFElXnXUQG5wsUC378cIf7xGDo8pljIh_A3QAcielLKR0DGNO5Xod68qknAstYazb0aulL_VT78z94TnRu_9E1siWrnlIoIFhgI2h4qUVxI2iG5WWDuio5Q930NHsbaKXutLDEtKNQHNi9G5Yg7JOl5SOHXP16kwIT___gGi_9g728DOiGqtvvfT5LIJCZoWQ7JDy01a_qpkEkk13Of5Lm5DyWNkUoEG__tntaEooCwf7NRQGbG0A '}, #calorie
        'api4' : { 'url': 'https://cosylab.iiitd.edu.in/rdbapi/recipeDB/searchRecipeByCarbs/195:196.5', 'token': a} #carbs
    }

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        if user_input.lower() in apis:
            api_info = apis[user_input.lower()]
            data = fetch_data_from_api(api_info['url'], api_info['token'])
            print("Data from API:", data)
        else:
            response = chatbot_response(user_input, api_key)
            print("Bot:", response)

if __name__ == "__main__":
    main()
