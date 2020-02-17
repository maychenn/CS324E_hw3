void setup() {
  size(800, 800);
  background(#ffffff);
  noLoop();
  redraw();
}

//colors
color yellow = color(255, 255, 0);
color black = color(0,0,0);

void draw() {
  String[] lines = loadStrings("wordfrequency.txt");
  
  //extracting the max word frequency (maxFreq) and the max freq of that word frequency (maxNum)
  String[] firstLine = lines[0].split(": ");

  String[] lastLine = lines[lines.length-1].split(": ");
  int maxNum = int(firstLine[1]);
  int maxFreq = int(lastLine[0]);
  
  //iterate through lines
  for (int i = 0; i < lines.length; i++) {
    //extracting the frequency & number of words of that frequency
    String [] stringFreq = lines[i].split(": ");
    int freq = int(stringFreq[0]);
    int num = int(stringFreq[1]);
    
    //color & stroke
    colorMode(HSB, maxFreq);
    //brightness proportional to frequency (modified for visibility)
    float brightness = (20 * freq);
    fill(yellow, brightness);
    strokeWeight(0.5);
    stroke(black);
    
    //rectangle
    //width equal for the span of the screen
    float w = 800.0 / lines.length;
    //height proportional to the number of words of that frequency
    float h = 800.0 * (num / maxNum);
    rect(i*w, 0, w, num);
  }
}
