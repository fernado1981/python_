# Let’s make sure you have the following libraries installed before we get started:
# ◻️ To create a word cloud: wordcloud
# ◻️ To import an image: pillow (will later import is as PIL)
# ◻️ To scrape text from Wikipedia: wikipedia
# Last package is optional, you can instead load up or create your own text data without having to pull text via web scraping.
# Import packages
import wikipedia
import re
import matplotlib.pyplot as plt


from wordcloud import WordCloud, STOPWORDS

# Specify the title of the Wikipedia page
wiki = wikipedia.page('Web scraping')
# Extract the plain text content of the page
text = wiki.content
# Clean text
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')


# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud)
    # No axis details
    plt.axis("off")


# Generate wordcloud
wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='black', colormap='Set2',
                      collocations=False, stopwords=STOPWORDS).generate(text)


# Plot
plot_cloud(wordcloud)

# Save image
wordcloud.to_file("wordcloud.png")
