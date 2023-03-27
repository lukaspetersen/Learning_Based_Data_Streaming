package code;

import java.util.ArrayList;
import java.util.List;

public class NewHeavyHitters {

    public CountMinSketch[] cms;
    private int n;

    public NewHeavyHitters(int n){
        this.n = n;
    }

    public static List<String> query(List<String> list, int i, int n, int j) {
        List<String> result = new ArrayList<>();
        result.add("empty value");
        return result;
    }

    public void update(int j, int delta) {
        for (int i = 0; i < 32; i++) {
            cms[i].add((int) (j / Math.floor(Math.pow(2, i))), delta);
        }
    }



}