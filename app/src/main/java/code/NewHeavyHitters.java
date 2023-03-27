package code;

import java.util.ArrayList;
import java.util.List;

public class NewHeavyHitters {

    public CountMinSketch[] cms;
    private int n;

    public NewHeavyHitters(int n){
        this.n = n;
    }

    public List<Integer> query(List<Integer> list, int n){
        return list;
    }


    public void queryFrom(List<Integer> list, int i, int n, int j) {

        int left = j*2;
        int right = j*2+1;

        if(i > 0){
            if(cms[i-1].estimateCount(left) >= n){
                queryFrom(list, i-1, n, j);
            }
            if(cms[i-1].estimateCount(right) >= n){
                queryFrom(list, i-1, n, j);
            }
            list.add(j);
        }
    }

    public void update(int j, int delta) {
        for (int i = 0; i < 32; i++) {
            cms[i].add((int) (j / Math.floor(Math.pow(2, i))), delta);
        }
    }



}