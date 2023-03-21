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

    public void add(String item){
        for(int i=0; i<hashFunctions; i++){
            int index = Math.abs(i*item.hashCode())%size; // Needs a better hash function
            bitSet.set(index, true);
        }
    }

    public String contains(String item){
        for(int i=0; i<hashFunctions; i++){
            int index = Math.abs(i*item.hashCode())%size;
            if(!bitSet.get(index)){
                return "Element not in set";
            }
        }
        return "Element in set";
    }

}
