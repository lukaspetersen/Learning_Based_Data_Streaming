package code;

import java.util.ArrayList;
import java.util.List;

public class NewHeavyHitters {

    public CountMinSketch[] cms;
    private int n;

    public NewHeavyHitters(int n){
        this.n = n;
    }

    public List<Integer> query(List<Integer> list){
        queryFrom(list, 2, this.n, 0);
        return list;
    }


    public void queryFrom(List<Integer> list, int i, int n, int x) {
        int left = x*2;
        int right = x*2+1;

        if(i > 0){
            if(cms[i-1].estimateCount(left) >= n){
                queryFrom(list, i-1, n, left);
            }
            if(cms[i-1].estimateCount(right) >= n){
                queryFrom(list, i-1, n, right);
            }
        }
        else{
            list.add(x);
        }
    }

    public void update(int j, int delta) {
        for (int i = 0; i < cms.length; i++) {
            cms[i].add((int) (j / Math.floor(Math.pow(2, i))), delta);
        }
    }



}