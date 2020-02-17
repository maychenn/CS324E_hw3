void setup() {
  size(1000, 1000);
  background(#ffffff);
  noLoop();
  redraw();
}

void draw() {
  String[] lines = loadStrings("wordfrequency.txt");
  //extracting the max word frequency (maxFreq) and the max freq of that word frequency (maxNum)
  String[] firstLine = lines[0].split(": ");

  String[] lastLine = lines[lines.length-1].split(": ");
  int maxNum = int(firstLine[1]);
  int maxFreq = int(lastLine[0]);
  println(maxFreq);
  //iterate through lines
  for (int i = lines.length-1; i >= 0; i--) {
    String [] stringFreq = lines[i].split(": ");
    int freq = int(stringFreq[0]);
    int num = int(stringFreq[1]);
    println(freq);
    // get color
    int yellow = (1-int(num / maxNum)) * 255;
    
    // get size
    float radius = (freq / maxFreq) * 1000;
    
    //draw circle
    fill(yellow, yellow, 0);
    strokeWeight(0.5);
    stroke(color(0,0,0));
    circle(500, 500, radius);
    
  }
  
  
  
  
  
  
  
}
