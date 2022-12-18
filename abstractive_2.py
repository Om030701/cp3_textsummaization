# Importing dependencies from transformers
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
# Load tokenizer
def abs_tifu_summary(raw_text):
    tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-cnn_dailymail")
    # Load model
    model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-cnn_dailymail")


    # Create tokens - number representation of our text
    tokens = tokenizer(raw_text, truncation=True, padding="longest", return_tensors="pt")

    summary = model.generate(**tokens)
    # Decode summary
    return (tokenizer.decode(summary[0]))
