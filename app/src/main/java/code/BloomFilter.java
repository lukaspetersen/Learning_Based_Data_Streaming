package code;

import java.util.BitSet;

public class BloomFilter {

    private final int size;
    private final int hashFunctions;
    private BitSet bitSet;


    public BloomFilter(int size, int hashFunctions){
        this.size = size;
        this.hashFunctions = hashFunctions;
        this.bitSet = new BitSet(size);
    }

    public void add(int item){
        for(int i=0; i<hashFunctions; i++){
            int index = Math.abs(i*item)%size; // Needs a better hash function
            bitSet.set(index, true);
        }
    }

    public String contains(int item){
        for(int i=0; i<hashFunctions; i++){
            int index = Math.abs(i*item)%size;
            if(!bitSet.get(index)){
                return "Element not in set";
            }
        }
        return "Element in set";
    }

}
