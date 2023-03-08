package code;

import java.nio.ByteBuffer;
import java.util.ArrayList;

public class HeavyHittersCountMin {

    private CountMinSketch countMinSketch;
    private ArrayList<String> heavyHitters;
    private int threshold;

    public HeavyHittersCountMin(int threshold, CountMinSketch countMinSketch, ArrayList<String> heavyHitters){
        this.threshold = threshold;
        this.countMinSketch = countMinSketch;
        this.heavyHitters = heavyHitters;
    }

    public void update(int item){
        int itemFrequency = countMinSketch.estimateCount(item);
        if(itemFrequency > threshold){
            byte[] originalBytes = ByteBuffer.allocate(4).putInt(item).array();
            String itemString = new String(originalBytes);
            heavyHitters.add(itemString);
        }
    }

    public ArrayList<String> query(){
        return heavyHitters;
    }


}



