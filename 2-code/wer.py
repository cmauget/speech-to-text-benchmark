import sys

def calc_wer(transcribed_text, original_text):
  # split the texts into lists of words
  transcribed_words = transcribed_text.split()
  original_words = original_text.split()

  # initialize the edit distance
  edit_distance = 0

  # iterate over the words in the original text
  for i, original_word in enumerate(original_words):
    # if the transcribed text is shorter than the original text, add the remaining words
    # in the original text to the edit distance
    if i >= len(transcribed_words):
      edit_distance += len(original_words) - i
      break

    # if the words are different, increment the edit distance
    if original_word != transcribed_words[i]:
      edit_distance += 1

  # return the WER as the edit distance divided by the number of words in the original text
  return edit_distance / len(original_words)

def main():
  # check that the correct number of command line arguments were provided
  if len(sys.argv) != 3:
    print("Usage: python wer.py transcribed_text_file original_text_file")
    return

  # read in the text from the files
  with open(sys.argv[1], "r") as f:
    transcribed_text = f.read()
  with open(sys.argv[2], "r") as f:
    original_text = f.read()

  # calculate the WER
  wer = calc_wer(transcribed_text, original_text)
  print("WER:", wer)

if __name__ == "__main__":
  main()
