PFont fontKano;
String[] uniqueWords;
color[] palette = {
  #A29E7E, //drab grey
  #FEFA3C, //yellow 
  #46440F, //dark olive
};

void setup() {
  size(700, 600);
  fontKano = createFont("Kano.otf", 30);
  textFont(fontKano);
  uniqueWords = loadStrings("uniquewords.txt");
  noLoop();
}

void draw() {
  background(#74763E); //light olive grey 
  int y = 0;
  int wordRandom; //random word
  int wordWidth;  //width of word in pixels
  //height - 31 instead of 30 due to letters clipping
  while(y <= (height - 31)) {
    wordRandom = int(random(uniqueWords.length));
    wordWidth = int(textWidth(uniqueWords[wordRandom]));
    y += 30;
    int x = 0;
    while(x < (width - wordWidth)) {
      populate(x, y, wordRandom);
      x += wordWidth + 10;
      wordRandom = int(random(uniqueWords.length));
      wordWidth = int(textWidth(uniqueWords[wordRandom]));
    }
  }
}

void populate(int x, int y, int random) {
  int wordLength = uniqueWords[random].length(); //character length of word
  //word color logic
  if(wordLength <= 5) {
    fill(palette[0]);
  } else if(wordLength <= 8) {
    fill(palette[2]);
  } else {
    fill(palette[1]);
  }
  //fill(palette[int(random(palette.length))]); //fills with random color
  text(uniqueWords[random], x, y); //choses random word from txt file
}

//mouse click, new selection of random, unique words will replace
void mousePressed() {
  redraw();
}
