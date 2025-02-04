package org.example;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.List;

import static org.mockito.Mockito.when;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.extension.ExtendWith;


//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    @ExtendWith(MockitoExtension.class)
    static
    class WhenTest {
        @Mock
        List mockList;

        @Test
        public void whenMockAnnotation() {
            //создаем правило: вернуть 10 при вызове метода size
            Mockito.when(mockList.size() ).thenReturn(10);

            //тут вызывается метод и вернет 10!!
            assertEquals(10, mockList.size());
        }
    }
}