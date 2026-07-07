import pandas as pd

data = {
    "email": [
        "Can we reschedule tomorroe's meeting?",
        "What is your refund policy?",
        "Do you offer team plans?"
    ],

    "reply": [
        "Sure, Friday works for me.",
        "Refunds are available within 30 days.",
        "Yes, we offer teams plan for organizations."
    ],

    "category": [
        "scheduling",
        "support",
        "sales"
    ]
}

df = pd.DataFrame(data)

print(df)

df.to_csv(
    "data/raw/email_reply_dataset.csv",
    index = False
)

print("Dataset saved successfully!")

print("\nFirst 2 rows")
print(df.head(2))

print("\nDataset shape")
print(df.shape)