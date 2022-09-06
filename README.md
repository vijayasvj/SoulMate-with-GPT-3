## Usage of Daisi

It is recommended to use this application on the daisi platform itself using the link https://app.daisi.io/daisies/vijay/Soul-Mate%20with%20GPT-3/app. However, you can still use your own editor using the below method:

### First, load the Packages:

```
import pydaisi as pyd
soul_mate_with_gpt_3 = pyd.Daisi("vijay/Soul-Mate with GPT-3")
```

### Now, connect to Daisi and access the functions using the following functions:

Lover:

```
soul_mate_with_gpt_3.lover(key, text).value
```

Friend:

```
soul_mate_with_gpt_3.friend(key, ftext).value
```

Mentor:

```
soul_mate_with_gpt_3.mentor(key, mtext).value
```

Relative:

```
soul_mate_with_gpt_3.relative(key, rtext).value
```

### In order to access Chatbot:

```
while text != "bye":
    reply = soul_mate_with_gpt_3.<botname>(key, text).value
    //Ex: reply = soul_mate_with_gpt_3.lover(key, text).value
    context = context + reply
    print(dna + reply)
    text = input("You: ")
    context = context + text
```

Use the above code to make the chatbot run until the input is "bye".

## And done! We have invoked our Chatbot!
