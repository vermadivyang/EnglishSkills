import matplotlib.pyplot as plt

def analyze_sentence_fluency(text):
    sentence_endings = ['.', '!', '?']
    sentences = []
    current_sentence = []

    for word in text.split():
        current_sentence.append(word)
        if any(current_sentence[-1].endswith(punctuation) for punctuation in sentence_endings):
            sentences.append(' '.join(current_sentence).strip())
            current_sentence = []
    
    if current_sentence:
        sentences.append(' '.join(current_sentence).strip())
    
    sentence_lengths = [len(sentence.split()) for sentence in sentences]
    avg_length = sum(sentence_lengths) / len(sentence_lengths)
    variance = sum((x - avg_length) ** 2 for x in sentence_lengths) / len(sentence_lengths)
    std_dev_length = variance ** 0.5
    
    return sentence_lengths, avg_length, std_dev_length

def plot_sentence_fluency(sentence_lengths, avg_length):
    # Create a line plot for sentence lengths
    plt.plot(sentence_lengths, marker='o', linestyle='-', color='b', label='Sentence Lengths')
    
    # Add a horizontal line at the average sentence length
    plt.axhline(y=avg_length, color='r', linestyle='--', label=f'Average Length ({avg_length:.2f} words)')
    
    # Title and labels
    plt.title('Sentence Lengths')
    plt.xlabel('Sentence Number')
    plt.ylabel('Number of Words')
    
    # Display legend
    plt.legend()
    
    # Add grid for better visualization
    plt.grid(True)
    
    # Show the plot
    plt.show()

def fluency_rating(avg_length, std_dev_length):
    if std_dev_length > 6:  # More variation is better, high standard deviation
        return "Excellent"
    elif 3 <= std_dev_length <= 6:
        return "Good"
    elif 1 <= std_dev_length < 3:
        return "Fair"
    else:
        return "Poor"

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None

def get_text():
    ADD_YOUR_TEXT_HERE = "Ambition. I was struggling with ambition. Wanting to do something useful or to achieve great things in life is something most decent humans strive for –but how do we do it? Each individual finds their answer, some work better than others. The solution many people find is to bury themselves in work –-to continue working until they get recognized for the almost infinite amount of tasks they try. One of my friends tries virtually every extracurricular activity: just so a good college can see him. Accomplishing complex and difficult tasks conveys our ambition, and shows that we did something with our life. It proves that we can be useful, we can do hard things. It sets us apart from the crowd, making us special –a feeling we all want."
    if ADD_YOUR_TEXT_HERE.strip():
        return ADD_YOUR_TEXT_HERE
    else:
        file_path = 'ExampleEssay.txt'
        text = read_text_from_file(file_path)
        if text:
            return text
        else:
            print(f"No text provided and no file found. Please provide text or ensure 'ExampleEssay.txt' is available.")
            return None

text = get_text()

if text:
    sentence_lengths, avg_length, std_dev_length = analyze_sentence_fluency(text)
    rating = fluency_rating(avg_length, std_dev_length)
    
    print(f"Average Sentence Length: {avg_length:.2f} words")
    print(f"Standard Deviation of Sentence Lengths: {std_dev_length:.2f} words")
    print(f"Sentence Fluency Rating: {rating}")
    
    plot_sentence_fluency(sentence_lengths, avg_length)
