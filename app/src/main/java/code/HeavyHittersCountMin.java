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

    public void update(String item){
        int itemFrequency = countMinSketch.estimateCount(item);
        if(itemFrequency > threshold){
            heavyHitters.add(item);
        }
    }

    public ArrayList<String> query(){
        return heavyHitters;
    }


}



