# multilingual_recommendations.py

RECOMMENDATIONS = {
    "Tomato_healthy": {
        "hi": {
            "advice": "आपकी टमाटर पौधा स्वस्थ है! सुझाव: सुबह जल्दी पानी दें, मिट्टी को नमी बनाए रखें, मल्चिंग करें, और कीटों के शुरुआकी लक्षणों के लिए साप्ताहिक निरीक्षण करें।",
            "pesticides": [],
            "fertilizers": ["NPK 10-10-10", "अच्छी तरह सड़ा हुआ खाद"],
            "dosage": "प्रति १०० वर्ग मीटर २ किलो उर्वरक मासिक रूप से दें।",
        },
        "en": {
            "advice": "Your tomato plant is healthy! Tips: Water early in the morning, keep the soil moist, use mulch, and inspect weekly for pests.",
            "pesticides": [],
            "fertilizers": ["NPK 10-10-10", "Well-rotted compost"],
            "dosage": "Apply fertilizer monthly at 2 kg per 100 sq.m.",
        },
        "bn": {
            "advice": "আপনার টমেটোর গাছ সুস্থ আছে! পরামর্শ: সকালে সকালে পানি দিন, মাটি আর্দ্র রাখুন, মাল্চ ব্যবহার করুন এবং কীটপতঙ্গ সপ্তাহে একবার পরীক্ষা করুন।",
            "pesticides": [],
            "fertilizers": ["NPK ১০-১০-১০", "ভালভাবে পচানো কম্পোস্ট"],
            "dosage": "প্রতি ১০০ বর্গমিটার মাসিক ২ কেজি সার প্রয়োগ করুন।",
        },
        "pa": {
            "advice": "ਤੁਹਾਡਾ ਟਮਾਟਰ ਪੌਦਾ ਸਿਹਤਮੰਦ ਹੈ! ਸੁਝਾਅ: ਸਵੇਰੇ ਜਲਦੀ ਪਾਣੀ ਦਿਓ, ਮਿੱਟੀ ਨੂੰ ਨਮੀਦਾਰ ਰੱਖੋ, ਮਲਚਿੰਗ ਕਰੋ, ਅਤੇ ਕੀੜਿਆਂ ਲਈ ਹਫਤਾਵਾਰੀ ਜਾਂਚ ਕਰੋ।",
            "pesticides": [],
            "fertilizers": ["NPK 10-10-10", "ਚੰਗੀ ਤਰ੍ਹਾਂ ਸੜਿਆ ਹੋਇਆ ਖਾਦ"],
            "dosage": "ਹਰ ਮਹੀਨੇ ੨ ਕੇਜੀ ਖਾਦ ੧੦੦ ਵਰਗ ਮੀਟਰ ਲਈ ਲਗਾਓ।",
        },
    },
    "Tomato_Bacterial_spot": {
        "hi": {
            "advice": "कॉपर-आधारित फंगीसाइड का उपयोग करें। संक्रमित पत्तियां हटा दें। फसल चक्रण और औजार साफ़ रखने का पालन करें।",
            "pesticides": ["Copper hydroxide", "Copper oxychloride"],
            "fertilizers": ["पोटैशियम सल्फेट"],
            "dosage": "हर १० दिनों में फंगीसाइड छिड़कें। १ लीटर पानी में २ ग्राम कॉपर हाइड्रॉक्साइड मिलाएं।",
        },
        "en": {
            "advice": "Use copper-based fungicides to control bacterial spot. Remove infected leaves and practice crop rotation.",
            "pesticides": ["Copper hydroxide", "Copper oxychloride"],
            "fertilizers": ["Potassium sulfate"],
            "dosage": "Spray fungicide every 10 days using 2 gm copper hydroxide per liter of water.",
        },
        "bn": {
            "advice": "ব্যাকটেরিয়াল স্পট নিয়ন্ত্রণের জন্য তামা-ভিত্তিক ফাঙ্গিসাইড ব্যবহার করুন। আক্রান্ত পাতা সরান এবং ফসল পরিবর্তন করুন।",
            "pesticides": ["কপার হাইড্রক্সাইড", "কপার অক্সিক্লোরাইড"],
            "fertilizers": ["পটাশিয়াম সালফেট"],
            "dosage": "প্রতি ১০ দিনে ১ লিটার পানিতে ২ গ্রাম কপার হাইড্রক্সাইড স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਤਾਂਬੇ ਆਧਾਰਿਤ ਫੰਗੀਸਾਈਡ ਵਰਤੋਂ ਕਰੋ। ਸੰਕ੍ਰਮਿਤ ਪੱਤੇ ਹਟਾਓ। ਫਸਲ ਫੇਰ ਬਦਲਾਅ ਅਤੇ ਸਾਫ ਸਫਾਈ ਜਾਰੀ ਰੱਖੋ।",
            "pesticides": ["ਤਾਂਬਾ ਹਾਈਡ੍ਰੋਆਕਸਾਈਡ", "ਤਾਂਬਾ ਆਕਸੀਕਲੋਰਾਈਡ"],
            "fertilizers": ["ਪੋਟੈਸ਼ੀਅਮ ਸੁਲਫੇਟ"],
            "dosage": "ਹਰ 10 ਦਿਨ ਬਾਅਦ ਫੰਗੀਸਾਈਡ ਛਿੜਕਾਓ। 1 ਲੀਟਰ ਪਾਣੀ ਵਿੱਚ 2 ਗ੍ਰਾਮ ਤਾਂਬਾ ਹਾਈਡ੍ਰੋਆਕਸਾਈਡ ਮਿਲਾਓ।",
        },
    },
    "Tomato_Early_blight": {
        "hi": {
            "advice": "च्लोरोथालोनिल या मैंकोजेब जैसे फंगीसाइड का उपयोग करें। संक्रमित पत्तियां हटा दें और पौधों के आस-पास हवा का संचार बढ़ाएं। प्राकृतिक उपाय: नीम तेल स्प्रे करें।",
            "pesticides": ["Chlorothalonil", "Mancozeb", "नीम तैल"],
            "fertilizers": ["संतुलित NPK उर्वरक"],
            "dosage": "७-१० दिनों के अंतराल पर स्प्रे लगाएं। निर्देशानुसार २ ग्राम प्रति लीटर पानी का उपयोग करें। नीम तेल हर ७ दिन में एक बार स्प्रे करें।",
        },
        "en": {
            "advice": "Apply fungicides such as chlorothalonil or mancozeb at the first sign of disease. Remove affected leaves and improve air circulation around plants. Natural treatment: Spray neem oil regularly.",
            "pesticides": ["Chlorothalonil", "Mancozeb", "Neem oil"],
            "fertilizers": ["Balanced NPK fertilizer"],
            "dosage": "Spray every 7-10 days. Use 2 gm/liter water following product label. Neem oil spray once a week.",
        },
        "bn": {
            "advice": "বিকলতা দেখা দিলে ক্লোরোথ্যালোনিল বা ম্যানকোজেব জাতীয় ফাঙ্গিসাইড ব্যবহার করুন। আক্রান্ত পাতা সরান এবং গাছের চারপাশে বায়ু সঞ্চালন বৃদ্ধি করুন। প্রাকৃতিক পদ্ধতি হিসেবে নিম তেল স্প্রে করুন।",
            "pesticides": ["Chlorothalonil", "Mancozeb", "নিম তেল"],
            "fertilizers": ["সন্তুলিত NPK সার"],
            "dosage": "৭-১০ দিনে স্প্রে করুন। নির্দেশ অনুসারে ২ গ্রাম প্রতি লিটার পানি ব্যবহার করুন। নিম তেল সপ্তাহে একবার স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਬੀਮਾਰੀ ਦੇ ਪਹਿਲੇ ਨਿਸ਼ਾਨ ਤੇ ਕਲੋਰੋਥੈਲੋਨੀਲ ਜਾਂ ਮੈਨਕੋਜ਼ੈਬ ਵਰਗੇ ਫੰਗੀਸਾਈਡ ਛਿੜਕਾਓ। ਸੰਕ੍ਰਮਿਤ ਪੱਤੇ ਹਟਾਓ ਅਤੇ ਪੌਦਿਆਂ ਦੇ ਆਲੇ ਦੁਆਲੇ ਹਵਾ ਦਾ ਪਰਿਵਾਹ ਵਧਾਓ। ਕੁਦਰਤੀ ਇਲਾਜ ਲਈ ਨੀਂਮ ਦਾ ਤੇਲ ਛਿੜਕਾਓ।",
            "pesticides": ["ਕਲੋਰੋਥੈਲੋਨੀਲ", "ਮੈਨਕੋਜ਼ੈਬ", "ਨੀਂਮ ਦਾ ਤੇਲ"],
            "fertilizers": ["ਸੰਤੁਲਿਤ NPK ਖਾਦ"],
            "dosage": "ਹਰ 7-10 ਦਿਨ ਬਾਅਦ ਛਿੜਕਾਓ। ਲੇਬਲ ਦੇ ਅਨੁਸਾਰ 2 ਗਰਾਮ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ ਵਰਤੋਂ। ਨੀਂਮ ਦੇ ਤੇਲ ਦੀ ਛਿੜਕਾਅ ਹਫਤੇ ਵਿੱਚ ਇੱਕ ਵਾਰੀ ਕਰੋ।",
        },
    },
    "Tomato_Late_blight": {
        "hi": {
            "advice": "मेटालैक्सिल जैसे फंगीसाइड का छिड़काव करें और संक्रमित पौधों को नष्ट करें। ओवरहेड पानी डालने से बचें।",
            "pesticides": ["Metalaxyl", "Copper oxychloride"],
            "fertilizers": ["आवश्यक होने पर कार्बनिक पोटैशियम डालें"],
            "dosage": "बारिश के बाद ७ दिनों के अंतराल पर स्प्रे करें। २ ग्राम प्रति लीटर पानी मिलाएं।",
        },
        "en": {
            "advice": "Spray with fungicides like metalaxyl and destroy infected plants. Avoid overhead watering and ensure good drainage.",
            "pesticides": ["Metalaxyl", "Copper oxychloride"],
            "fertilizers": ["Add organic potassium if needed"],
            "dosage": "Spray every 7 days after rain or irrigation using 2 gm/liter water.",
        },
        "bn": {
            "advice": "মেটালাক্সিল জাতীয় ফাঙ্গিসাইড স্প্রে করুন এবং আক্রান্ত গাছগুলি ধ্বংস করুন। উপরের দিকে পানি দেওয়া এড়িয়ে চলুন।",
            "pesticides": ["Metalaxyl", "Copper oxychloride"],
            "fertilizers": ["প্রয়োজন হলে জৈব পটাশিয়াম যোগ করুন"],
            "dosage": "বৃষ্টি বা সেচের পর ৭ দিনে একবার স্প্রে করুন। ২ গ্রাম প্রতি লিটার পানি ব্যবহার করুন।",
        },
        "pa": {
            "advice": "ਮੇਟਾਲੈਕਸਿਲ ਵਰਗੇ ਫੰਗੀਸਾਈਡ ਨਾਲ ਛਿੜਕਾਅ ਕਰੋ ਅਤੇ ਸੰਕ੍ਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਨਸ਼ਟ ਕਰੋ। ਓਵਰਹੈੱਡ ਪਾਣੀ ਦੇਣ ਤੋਂ ਬਚੋ।",
            "pesticides": ["ਮੇਟਾਲੈਕਸਿਲ", "ਤਾਂਬਾ ਆਕਸੀਕਲੋਰਾਈਡ"],
            "fertilizers": ["ਲੋੜ ਹੋਣ ਤੇ ਜੈਵਿਕ ਪੋਟੈਸ਼িয়ਮ ਸ਼ਾਮਲ ਕਰੋ"],
            "dosage": "ਬਰਸਾਤ ਜਾਂ ਸেচ ਤੋਂ ਬਾਅਦ ਹਰ 7 ਦਿਨ ਛਿੜਕਾਓ। 2 ਗ੍ਰਾਮ ਪ੍ਰਤੀ ਲੀਟਰ ਪਾਣੀ ਵਰਤੋਂ।",
        },
    },
    "Tomato_Leaf_Mold": {
        "hi": {
            "advice": "हवा का संचार बढ़ाएं, पत्तियों पर पानी डालने से बचें, और आवश्यकता पड़ने पर क्लोरोथालोनिल जैसे फंगीसाइड लगाएं।",
            "pesticides": ["Chlorothalonil", "Copper oxychloride"],
            "fertilizers": ["सामान्य NPK"],
            "dosage": "निचली पत्तियों पर १० दिनों के अंतराल पर स्प्रे लगाएं।",
        },
        "en": {
            "advice": "Increase air circulation, avoid watering leaves, and apply fungicides like chlorothalonil if needed.",
            "pesticides": ["Chlorothalonil", "Copper oxychloride"],
            "fertilizers": ["General NPK"],
            "dosage": "Spray on lower leaf surfaces every 10 days.",
        },
        "bn": {
            "advice": "বায়ু সঞ্চালন বাড়ান, পাতা র ওপর পানি দেবেন না, এবং প্রয়োজনে ক্লোরোথ্যালোনিল জাতীয় ফাঙ্গিসাইড স্প্রে করুন।",
            "pesticides": ["Chlorothalonil", "Copper oxychloride"],
            "fertilizers": ["সাধারণ NPK সার"],
            "dosage": "১০ দিনে একবার পাতার নীচে স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਹਵਾ ਦਾ ਪਰਿਵਾਹ ਵਧਾਓ, ਪੱਤਿਆਂ 'ਤੇ ਪਾਣੀ ਦੇਣ ਤੋਂ ਬਚੋ, ਅਤੇ ਲੋੜ ਹੋਣ 'ਤੇ ਕਲੋਰੋਥੈਲੋਨੀਲ ਵਰਗੇ ਫੰਗੀਸਾਈਡ ਛਿੜਕਾਓ।",
            "pesticides": ["ਕਲੋਰੋਥੈਲੋਨੀਲ", "ਤਾਂਬਾ ਆਕਸੀਕਲੋਰਾਈਡ"],
            "fertilizers": ["ਆਮ NPK ਖਾਦ"],
            "dosage": "ਹਰ 10 ਦਿਨ ਪੱਤਿਆਂ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ 'ਤੇ ਛਿੜਕਾਓ।",
        },
    },
    "Tomato_Septoria_leaf_spot": {
        "hi": {
            "advice": "संक्रमित पत्तियां हटा दें और मैंकोजेब जैसे फंगीसाइड लगाएं। पौधों को जमीनी स्तर पर पानी दें। मल्चिंग करें।",
            "pesticides": ["Mancozeb", "Chlorothalonil"],
            "fertilizers": ["खाद"],
            "dosage": "७ दिनों के अंतराल पर छिड़काव करें।",
        },
        "en": {
            "advice": "Remove infected leaves and use fungicides such as mancozeb. Water plants at soil level and use mulch to prevent soil splash.",
            "pesticides": ["Mancozeb", "Chlorothalonil"],
            "fertilizers": ["Compost"],
            "dosage": "Spray every 7 days as per label instructions.",
        },
        "bn": {
            "advice": "আক্রান্ত পাতা সরান এবং ম্যানকোজেব জাতীয় ফাঙ্গিসাইড ব্যবহার করুন। গাছকে মাটি স্তরে পানি দিন এবং মাল্চ ব্যবহার করুন।",
            "pesticides": ["Mancozeb", "Chlorothalonil"],
            "fertilizers": ["কম্পোস্ট"],
            "dosage": "হাতে লেবেল অনুসারে ৭ দিনে একবার স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਸੰਕ੍ਰਮਿਤ ਪੱਤੇ ਹਟਾਓ ਅਤੇ ਮੈਨਕੋਜ਼ੈਬ ਵਰਗੇ ਫੰਗੀਸਾਈਡ ਛਿੜਕਾਓ। ਪੌਦਿਆਂ ਨੂੰ ਮਿੱਟੀ ਦੇ ਸਤਰ 'ਤੇ ਪਾਣੀ ਦਿਓ ਅਤੇ ਮਲਚ ਵਰਤੋਂ।",
            "pesticides": ["ਮੈਨਕੋਜ਼ੈਬ", "ਕਲੋਰੋਥੈਲੋਨੀਲ"],
            "fertilizers": ["ਖਾਦ"],
            "dosage": "ਹਰ 7 ਦਿਨ ਬਾਅਦ ਛਿੜਕਾਓ।",
        },
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "hi": {
            "advice": "माइटिसाइड या कीटनाशक साबुन का उपयोग करें। पौधों के आसपास नमी बढ़ाएं। हल्की संक्रमण के लिए पानी से पत्ते धोएं। प्राकृतिक विकल्प: नीम आधारित कीटनाशक।",
            "pesticides": ["Abamectin", "Insecticidal soap", "नीम आधारित कीटनाशक"],
            "fertilizers": ["संतुलित तरल उर्वरक"],
            "dosage": "निर्दिष्ट अनुसार माइटिसाइड का उपयोग करें। आवश्यकतानुसार दोहराएं।",
        },
        "en": {
            "advice": "Spray with miticides or use insecticidal soap. Increase humidity around plants. For mild infestations, wash leaves with water. Natural option: neem-based insecticide.",
            "pesticides": ["Abamectin", "Insecticidal soap", "Neem-based insecticide"],
            "fertilizers": ["Balanced liquid fertilizer"],
            "dosage": "Use miticides as directed. Repeat as needed.",
        },
        "bn": {
            "advice": "মাইটিসাইড দিয়ে স্প্রে করুন অথবা কীটনাশক সাবান ব্যবহার করুন। গাছের চারপাশে আর্দ্রতা বাড়ান। হালকা প্রভাবের ক্ষেত্রে পাতা ধুয়ে ফেলুন। প্রাকৃতিক বিকল্প: নিম-ভিত্তিক কীটনাশক।",
            "pesticides": ["Abamectin", "Insecticidal soap", "নিম-ভিত্তিক কীটনাশক"],
            "fertilizers": ["সন্তুলিত তরল সার"],
            "dosage": "নির্দেশ অনুসারে মাইটিসাইড ব্যবহার করুন। প্রয়োজনে পুনরায় প্রয়োগ করুন।",
        },
        "pa": {
            "advice": "ਮਾਈਟਿਸਾਈਡ ਨਾਲ ਛਿੜਕਾਓ ਜਾਂ ਕੀਟਨਾਸ਼ਕ ਸਾਬਣ ਵਰਤੋਂ। ਪੌਦਿਆਂ ਦੇ ਆਲੇ ਦੁਆਲੇ ਨਮੀ ਵਧਾਓ। ਹਲਕੇ ਸੰਕਰਮਣ ਲਈ ਪੱਤਿਆਂ ਨੂੰ ਪਾਣੀ ਨਾਲ ਧੋਵੋ। ਕੁਦਰਤੀ ਵਿਕਲਪ: ਨੀਂਮ-ਆਧਾਰਿਤ ਕੀਟਨਾਸ਼ਕ।",
            "pesticides": ["ਅਬਾਮੈਕਟਿਨ", "ਕੀਟਨਾਸ਼ਕ ਸਾਬਣ", "ਨੀਂਮ-ਆਧਾਰਿਤ ਕੀਟਨਾਸ਼ਕ"],
            "fertilizers": ["ਸੰਤੁਲਿਤ ਤਰਲ ਖਾਦ"],
            "dosage": "ਨਿਰਦੇਸ਼ਾਂ ਮੁਤਾਬਕ ਮਾਈਟਿਸਾਈਡ ਵਰਤੋਂ। ਲੋੜ ਅਨੁਸਾਰ ਦੁਹਰਾਓ।",
        },
    },
    "Tomato_Target_Spot": {
        "hi": {
            "advice": "संक्रमित पत्तियां हटा दें और क्लोरोथालोनिल या कॉपर ऑक्सीक्लोराइड जैसे फंगीसाइड लगाएं।",
            "pesticides": ["Chlorothalonil", "Copper oxychloride"],
            "fertilizers": ["नाइट्रोजन-युक्त उर्वरक"],
            "dosage": "७ दिनों के अंतराल पर छिड़काव करें।",
        },
        "en": {
            "advice": "Remove infected leaves and apply fungicides such as chlorothalonil or copper oxychloride.",
            "pesticides": ["Chlorothalonil", "Copper oxychloride"],
            "fertilizers": ["Nitrogen-rich fertilizer"],
            "dosage": "Spray every 7 days following product labels.",
        },
        "bn": {
            "advice": "আক্রান্ত পাতা সরান এবং ক্লোरोথ্যালোনিল বা কপার অক্সিক্লোরাইড জাতীয় ফাঙ্গিসাইড স্প্রে করুন।",
            "pesticides": ["Chlorothalonil", "Copper oxychloride"],
            "fertilizers": ["নাইট্রোজেন সমৃদ্ধ সার"],
            "dosage": "সপ্তাহে একবার স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਸੰਕ੍ਰਮਿਤ ਪੱਤੇ ਹਟਾਓ ਅਤੇ ਕਲੋਰੋਥੈਲੋਨੀਲ ਜਾਂ ਤਾਂਬਾ ਆਕਸੀਕਲੋਰਾਈਡ ਵਰਗੇ ਫੰਗੀਸਾਈਡ ਛਿੜਕਾਓ।",
            "pesticides": ["ਕਲੋਰੋਥੈਲੋਨੀਲ", "ਤਾਂਬਾ ਆਕਸੀਕਲੋਰਾਈਡ"],
            "fertilizers": ["ਨਾਈਟ੍ਰੋਜਨ-ਧਨ ਖਾਦ"],
            "dosage": "ਹਰ 7 ਦਿਨ ਬਾਅਦ ਛਿੜਕਾਓ।",
        },
    },
    "Tomato_Tomato_mosaic_virus": {
        "hi": {
            "advice": "कोई रासायनिक उपचार नहीं। संक्रमित पौधों को हटा दें। हाथ और औजार साफ़ करें।",
            "pesticides": [],
            "fertilizers": ["प्रतिरक्षा बढ़ाने हेतु खाद"],
            "dosage": "सभी उपकरण साफ करें।",
        },
        "en": {
            "advice": "No chemical cure. Remove and destroy infected plants. Disinfect hands and tools after handling plants.",
            "pesticides": [],
            "fertilizers": ["Compost to boost immunity"],
            "dosage": "Sanitize all tools after contact.",
        },
        "bn": {
            "advice": "কোনও রাসায়নিক চিকিৎসা নেই। আক্রান্ত গাছ সরিয়ে ফেলুন। হাত এবং সরঞ্জাম জীবাণুমুক্ত করুন।",
            "pesticides": [],
            "fertilizers": ["প্রতিরোধ ক্ষমতা বাড়ানোর জন্য কম্পোস্ট"],
            "dosage": "সকল সরঞ্জাম পরিষ্কার করুন।",
        },
        "pa": {
            "advice": "ਕੋਈ ਰਸਾਇਣਕ ਇਲਾਜ ਨਹੀਂ। ਸੰਕ੍ਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਹਟਾਓ। ਹੱਥਾਂ ਅਤੇ ਸਾਧਨਾਂ ਨੂੰ ਸਾਫ਼ ਕਰੋ।",
            "pesticides": [],
            "fertilizers": ["ਇਮਿਉਨਿਟੀ ਵਧਾਉਣ ਲਈ ਖਾਦ"],
            "dosage": "ਸਾਰੇ ਸੰਦ ਸਾਫ਼ ਕਰੋ।",
        },
    },
    "Tomato_Tomato_YellowLeaf_Curl_Virus": {
        "hi": {
            "advice": "संक्रमित पौधों को हटा दें। सफेद मक्खियों को नीम के तेल या पीले चिपचिपे जाल से नियंत्रित करें।",
            "pesticides": ["Neem oil", "Imidacloprid (सावधानी से प्रयोग करें)"],
            "fertilizers": ["पोटैशियम युक्त उर्वरक"],
            "dosage": "नियमित रूप से नीम का तेल छिड़कें।",
        },
        "en": {
            "advice": "Remove infected plants. Control whiteflies with neem oil or yellow sticky traps. Use resistant varieties if available.",
            "pesticides": ["Neem oil", "Imidacloprid (use cautiously)"],
            "fertilizers": ["Potassium-rich fertilizer"],
            "dosage": "Spray neem oil weekly following label instructions.",
        },
        "bn": {
            "advice": "আক্রান্ত গাছ সরিয়ে ফেলুন। সাদা মাছি নিয়ন্ত্রণ করতে নিম তেল বা হলুদ স্টিকি ট্র্যাপ ব্যবহার করুন।",
            "pesticides": ["Neem oil", "Imidacloprid (সাবধানতার সঙ্গে ব্যবহার করুন)"],
            "fertilizers": ["পটাশিয়াম সমৃদ্ধ সার"],
            "dosage": "নিয়মিত নিম তেল স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਸੰਕ੍ਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਹਟਾਓ। ਸਫੈਦ ਮੱਖੀਆਂ ਨੂੰ ਨੀਂਮ ਦੇ ਤੇਲ ਜਾਂ ਪੀਲੇ ਚਿਪਚਿਪੇ ਜਾਲ ਨਾਲ ਕਾਬੂ ਕਰੋ। ਲਗਦਾਰ ਪਰਕਾਰ ਵਰਤੋਂ ਜੇ ਉਪਲਬਧ ਹੋਵੇ।",
            "pesticides": ["ਨੀਂਮ ਦਾ ਤੇਲ", "ਇਮੀਡਾਕਲੋਪ੍ਰਿਡ (ਸਾਵਧਾਨੀ ਨਾਲ ਵਰਤੋਂ)"],
            "fertilizers": ["ਪੋਟੈਸ਼ੀਅਮ-ਧਰ ਖਾਦ"],
            "dosage": "ਨੀਂਮ ਦਾ ਤੇਲ ਹਫਤੇ ਵਿੱਚ ਇੱਕ ਵਾਰੀ ਲਗਾਓ।",
        },
    },
    "Pepper__bell___Bacterial_spot": {
        "hi": {
            "advice": "कॉपर-आधारित जीवाणुनाशक का उपयोग करें। संक्रमित पौधों को हटा दें। फसल चक्रण और ओवरहेड सिंचाई से बचें।",
            "pesticides": ["Copper hydroxide"],
            "fertilizers": ["पोटैशियम नाइट्रेट"],
            "dosage": "१०-१४ दिनों के अंतराल पर छिड़काव करें।",
        },
        "en": {
            "advice": "Use copper-based bactericides. Remove infected plants. Practice crop rotation and avoid overhead irrigation.",
            "pesticides": ["Copper hydroxide"],
            "fertilizers": ["Potassium nitrate"],
            "dosage": "Spray every 10-14 days as needed.",
        },
        "bn": {
            "advice": "কপার-ভিত্তিক ব্যাকটেরিয়া নিয়ন্ত্রণ ব্যবস্থা ব্যবহার করুন। আক্রান্ত গাছ সরিয়ে ফেলুন। ফসল পরিবর্তন করুন এবং উপরে পানি দেওয়া এড়িয়ে চলুন।",
            "pesticides": ["Copper hydroxide"],
            "fertilizers": ["Potassium nitrate"],
            "dosage": "প্রয়োজন অনুযায়ী ১০-১৪ দিনে একবার স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਤਾਂਬਾ ਆਧਾਰਿਤ ਜੀਵਾਣੂ ਨਾਸ਼ਕ ਵਰਤੋਂ। ਸੰਕ੍ਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਹਟਾਓ। ਫਸਲ ਬਦਲਾਅ ਕਰੋ ਅਤੇ ਓਵਰਹੈਡ ਸਿੰਚਾਈ ਤੋਂ ਬਚੋ।",
            "pesticides": ["ਤਾਂਬਾ ਹਾਈਡ੍ਰੋਕਸੀਡ"],
            "fertilizers": ["ਪੋਟੈਸ਼ੀਅਮ ਨਾਈਟਰੇਟ"],
            "dosage": "ਜਰੂਰਤ ਅਨੁਸਾਰ 10-14 ਦਿਨਾਂ 'ਚ ਇੱਕ ਵਾਰੀ ਛਿੜਕਾਓ।",
        },
    },
    "Pepper__bell___healthy": {
        "hi": {
            "advice": "आपका शिमला मिर्च का पौधा स्वस्थ है! मिट्टी की नमी जांचें, कीटों के लिए साप्ताहिक निरीक्षण करें, और संतुलित उर्वरक लगाएं।",
            "pesticides": [],
            "fertilizers": ["सामान्य NPK", "जैविक खाद"],
            "dosage": "प्रति पौधे १०० ग्राम एनपीके मासिक रूप से लगाएं।",
        },
        "en": {
            "advice": "Your bell pepper plant is healthy! Tips: Check soil moisture, inspect weekly for pests, mulch around the base, and apply balanced fertilizer.",
            "pesticides": [],
            "fertilizers": ["All-purpose NPK", "Organic manure"],
            "dosage": "Apply 100g NPK per plant monthly.",
        },
        "bn": {
            "advice": "আপনার বেল মরিচ গাছ সুস্থ আছে! মাটির আর্দ্রতা পরীক্ষা করুন, কীটপতঙ্গের জন্য সপ্তাহে একবার নিরীক্ষণ করুন, এবং সুষম সার ব্যবহার করুন।",
            "pesticides": [],
            "fertilizers": ["সাধারণ NPK সার", "জৈব সার"],
            "dosage": "প্রতি গাছে মাসে ১০০ গ্রাম সার দিন।",
        },
        "pa": {
            "advice": "ਤੁਹਾਡਾ ਬੈੱਲ ਮਿਰਚ ਦਾ ਪੌਦਾ ਸਿਹਤਮੰਦ ਹੈ! ਮਿੱਟੀ ਦੀ ਨਮੀ ਚੈਕ ਕਰੋ, ਹਫਤੇ ਵਿੱਚ ਇੱਕ ਵਾਰੀ ਕੀੜਿਆਂ ਲਈ ਜਾਂਚ ਕਰੋ, ਅਤੇ ਸੰਤੁਲਿਤ ਖਾਦ ਲਗਾਓ।",
            "pesticides": [],
            "fertilizers": ["ਸਾਰਾ ਉਦੇਸ਼ NPK", "ਜੈਵਿਕ ਖਾਦ"],
            "dosage": "ਹਰ ਮਹੀਨੇ 100 ਗ੍ਰਾਮ NPK ਪ੍ਰਤੀ ਪੌਦਾ ਲਗਾਓ।",
        },
    },
    "Potato___Early_blight": {
        "hi": {
            "advice": "संक्रमित पत्तियां हटाएं और मैंकोजेब या क्लोरोथालोनिल जैसे फंगीसाइड लगाएं। पत्तियों को गीला न करें।",
            "pesticides": ["Mancozeb", "Chlorothalonil"],
            "fertilizers": ["खाद", "पोटैशियम उर्वरक"],
            "dosage": "पहली लक्षण दिखते ही ७-१० दिनों में छिड़काव करें।",
        },
        "en": {
            "advice": "Remove infected leaves and use fungicides such as mancozeb or chlorothalonil. Avoid wetting foliage.",
            "pesticides": ["Mancozeb", "Chlorothalonil"],
            "fertilizers": ["Compost", "Potassium fertilizer"],
            "dosage": "Spray every 7-10 days starting at first symptoms.",
        },
        "bn": {
            "advice": "আক্রান্ত পাতা সরান এবং ম্যানকোজেব বা ক্লোরোথ্যালোনিল জাতীয় ফাঙ্গিসাইড ব্যবহার করুন। পাতা ভেজানো এড়িয়ে চলুন।",
            "pesticides": ["Mancozeb", "Chlorothalonil"],
            "fertilizers": ["কম্পোস্ট", "পটাশিয়াম সার"],
            "dosage": "প্রথম লক্ষণ দেখা দিলে ৭-১০ দিনে একবার স্প্রে করুন।",
        },
        "pa": {
            "advice": "ਸੰਕ੍ਰਮਿਤ ਪੱਤੇ ਹਟਾਓ ਅਤੇ ਮੈਨਕੋਜ਼ੈਬ ਜਾਂ ਕਲੋਰੋਥੈਲੋਨੀਲ ਵਰਗੇ ਫੰਗੀਸਾਈਡ ਛਿੜਕਾਓ। ਪੱਤਿਆਂ ਨੂੰ ਗਿੱਲਾ ਕਰਨ ਤੋਂ ਬਚੋ।",
            "pesticides": ["ਮੈਨਕੋਜ਼ੈਬ", "ਕਲੋਰੋਥੈਲੋਨੀਲ"],
            "fertilizers": ["ਖਾਦ", "ਪੋਟੈਸ਼ੀਅਮ ਖਾਦ"],
            "dosage": "ਪਹਿਲੇ ਲੱਛਣਾ ਤੇ 7-10 ਦਿਨਾਂ 'ਚ ਇੱਕ ਵਾਰੀ ਛਿੜਕਾਓ।",
        },
    },
    "Potato___Late_blight": {
        "hi": {
            "advice": "७-दिन के अंतराल पर कवकनाशक का छिड़काव करें। संक्रमित पौधों को उखाड़कर नष्ट करें।",
            "pesticides": ["Cymoxanil", "Mancozeb"],
            "fertilizers": ["संतुलित NPK"],
            "dosage": "बारिश से पहले और बाद में स्प्रे करें।",
        },
        "en": {
            "advice": "Spray protectant fungicides (e.g., cymoxanil) at 7-day intervals. Uproot and destroy affected plants.",
            "pesticides": ["Cymoxanil", "Mancozeb"],
            "fertilizers": ["Balanced NPK"],
            "dosage": "Apply as per fungicide label. Start sprays before disease appears in wet weather.",
        },
        "bn": {
            "advice": "৭ দিনে একবার সিমোক্সানিল জাতীয় ফাঙ্গিসাইড স্প্রে করুন। আক্রান্ত গাছটি তুলে ফেলুন এবং ধ্বংস করুন।",
            "pesticides": ["Cymoxanil", "Mancozeb"],
            "fertilizers": ["সন্তুলিত NPK সার"],
            "dosage": "বৃষ্টির আগেই স্প্রে শুরু করুন।",
        },
        "pa": {
            "advice": "ਹਰ 7 ਦਿਨ ਬਾਅਦ ਸਿਯਮੋਕਸਾਨਿਲ ਵਰਗਾ ਫੰਗੀਸਾਈਡ ਛਿੜਕਾਓ। ਸੰਕ੍ਰਮਿਤ ਪੌਦਿਆਂ ਨੂੰ ਉਖਾੜ ਕੇ ਨਸ਼ਟ ਕਰੋ।",
            "pesticides": ["ਸਿਮੋਕਸਾਨਿਲ", "ਮੈਨਕੋਜ਼ੈਬ"],
            "fertilizers": ["ਸੰਤੁਲਿਤ NPK"],
            "dosage": "ਬਾਰਿਸ਼ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਬਾਅਦ ਛਿੜਕਾਉ ਸ਼ੁਰੂ ਕਰੋ।",
        },
    },
    "Potato___healthy": {
        "hi": {
            "advice": "आपका आलू का पौधा स्वस्थ है! स्टेम के चारों ओर मिट्टी उठाएं, नियमित पानी दें, ब्लाइट के संकेत देखें, और मुल्च करें।",
            "pesticides": [],
            "fertilizers": ["आलू-विशिष्ट NPK", "लकड़ी की राख"],
            "dosage": "बुवाई पर खाद डालें; अंकुरण पर एक बार उर्वरक दें।",
        },
        "en": {
            "advice": "Your potato plant is healthy! Hill soil around stems, water consistently, watch for blight signs, and mulch roots.",
            "pesticides": [],
            "fertilizers": ["Potato-specific NPK", "Wood ash (for K)"],
            "dosage": "Apply compost at planting; fertilize once at emergence.",
        },
        "bn": {
            "advice": "আপনার আলুর গাছ সুস্থ আছে! গাছের চারপাশে মাটি উঠান, নিয়মিত পানি দিন, ব্লাইট লক্ষণ পরীক্ষা করুন এবং মাল্চ ব্যবহার করুন।",
            "pesticides": [],
            "fertilizers": ["আলু-নির্দিষ্ট NPK", "কাঠের ছাই"],
            "dosage": "রোপণের সময় কম্পোস্ট দিন; অঙ্কুরে একবার সার দিন।",
        },
        "pa": {
            "advice": "ਤੁਹਾਡਾ ਆਲੂ ਦਾ ਪੌਦਾ ਸਿਹਤਮੰਦ ਹੈ! ਸਟੈਮ ਦੇ ਆਲੇ ਦੁਆਲੇ ਮਿੱਟੀ ਉਠਾਓ, ਨਿਯਮਿਤ ਪਾਣੀ ਦਿਓ, ਬਲਾਈਟ ਦੇ ਲੱਛਣ ਵੇਖੋ ਅਤੇ ਮਲਚ ਕਰੋ।",
            "pesticides": [],
            "fertilizers": ["ਆਲੂ ਖਾਸ NPK", "ਕਾਠ ਦੀ ਰੱਖ"],
            "dosage": "ਰੋਪਣ ਵੇਲੇ ਖਾਦ ਲਗਾਓ; ਅੰਕੁਰਣ ਤੇ ਇੱਕ ਵਾਰੀ ਖਾਦ ਦਿਓ।",
        },
    },
}

# Translated labels for output
LABELS = {
    "hi": {"advice": "सलाह", "pesticides": "कीटनाशक", "fertilizers": "उर्वरक", "dosage": "खुराक"},
    "en": {"advice": "Advice", "pesticides": "Pesticides", "fertilizers": "Fertilizers", "dosage": "Dosage"},
    "bn": {"advice": "পরামর্শ", "pesticides": "কীটনাশক", "fertilizers": "সার", "dosage": "মাত্রা"},
    "pa": {"advice": "ਸਲਾਹ", "pesticides": "ਕੀਟਨਾਸ਼ਕ", "fertilizers": "ਖਾਦ", "dosage": "ਖੁਰਾਕ"},
}

def get_recommendation(disease_class, lang='en'):
    disease_info = RECOMMENDATIONS.get(disease_class)
    if disease_info and lang in disease_info:
        return disease_info[lang]
    elif disease_info:
        return disease_info.get('en', {})
    else:
        return {
            "advice": {
                "hi": "इस रोग के लिए कोई सिफारिश उपलब्ध नहीं है। कृपया कृषि विशेषज्ञ से संपर्क करें।",
                "en": "No specific recommendation available. Consult local agricultural extension services.",
                "bn": "এই রোগের জন্য কোনো সুপারিশ উপলব্ধ নেই। স্থানীয় কৃষি অফিসের সাথে যোগাযোগ করুন।",
                "pa": "ਇਸ ਰੋਗ ਲਈ ਕੋਈ ਸਿਫਾਰਿਸ਼ ਉਪਲਬਧ ਨਹੀਂ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਕਿਸਾਨ ਸਹਾਇਤਾ ਕੇਂਦਰ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।",
            }.get(lang, "No recommendation available."),
            "pesticides": [],
            "fertilizers": [],
            "dosage": "",
        }

if __name__ == "__main__":
    # Test all diseases and languages including Punjabi with translated labels:
    for disease in RECOMMENDATIONS:
        print(f"\n--- Recommendations for {disease} ---")
        for language in ['hi', 'en', 'bn', 'pa']:
            print(f"\nLanguage: {language}")
            rec = get_recommendation(disease, language)
            for k, v in rec.items():
                label = LABELS.get(language, LABELS['en']).get(k, k.capitalize())
                print(f"{label}: {v}")