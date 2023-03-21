package code;
import java.util.Random;

class CountMinSketch {
    private final int[][] table;
    private final int[] hashA; // long
    private final int[] hashB; // long
    private final int depth;
    private final int width;
    private final int prime; // long
    private final Random rand;

    public CountMinSketch(int depth, int width, int prime) {
        this.depth = depth;
        this.width = width;
        this.prime = prime;
        table = new int[depth][width];
        hashA = new int[depth];
        hashB = new int[depth];
        rand = new Random();

        for (int i = 0; i < depth; i++) {
            hashA[i] = rand.nextInt(prime - 1) + 1; // prime - 1 to make hash value is smaller than prime later
            hashB[i] = rand.nextInt(prime - 1);
        }
    }

    public void add(String item, int count) {
        for (int i = 0; i < depth; i++) {
            int index = (hashA[i] * item.hashCode() + hashB[i]) % prime; // index long
            index = Math.floorMod(index, width);
            table[i][index] += count;
        }
    }

    public int estimateCount(String item) {
        int minCount = Integer.MAX_VALUE;
        for (int i = 0; i < depth; i++) {
            int index = (hashA[i] * item.hashCode() + hashB[i]) % prime;
            index = Math.floorMod(index, width);
            minCount = Math.min(minCount, table[i][index]);
        }
        return minCount;
    }


}