void setup() {
  size(1000, 1000);
  background(#74763E);
  noLoop();
  redraw();
}

void draw() {
  String[] lines = loadStrings("wordfrequency.txt");
  print(lines[1]);
  //extracting the max word frequency (maxFreq) and the max freq of that word frequency (maxNum)
  String[] firstLine = lines[0].split(": ");

  String[] lastLine = lines[lines.length-1].split(": ");
  int maxNum = int(firstLine[0]);
  int maxFreq = int(lastLine[0]);
  
  //iterate through lines
  for (int i = 0; i < lines.length; i++) {
    String [] stringFreq = lines[i].split(": ");
    int num = int(stringFreq[0]);
    int freq = int(stringFreq[1]);
    
    // get color
    int yellow = int(freq / maxFreq) * 255;
    color c = color(0, yellow, 0);
    
    // get size
    float radius = (num / maxNum) * 1000;
    
    //draw circle
    fill(c, 191);
    stroke(color(0,0,0));
    circle(500, 500, radius);
    
  }
  
  
  
  
  
  
  
}
