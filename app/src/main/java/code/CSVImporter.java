package code;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class CSVImporter {
    public static String[] importCSV(String filePath, int columnIndex) throws IOException {
        List<String> columnValues = new ArrayList<>();

        try (FileReader reader = new FileReader(filePath)) {
            CSVParser parser = new CSVParser(reader, CSVFormat.DEFAULT);
            for (CSVRecord record : parser) {
                columnValues.add(record.get(columnIndex));
            }
        }

        return columnValues.toArray(new String[0]);
    }
}