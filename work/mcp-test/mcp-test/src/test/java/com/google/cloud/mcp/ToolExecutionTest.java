package com.google.cloud.mcp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.Collections;
import java.util.Map;
import java.util.concurrent.CompletableFuture;
import org.junit.jupiter.api.Test;

public class ToolExecutionTest {

    @Test
    public void testExecuteToolSuccess() throws Exception {
        McpToolboxClient mockClient = mock(McpToolboxClient.class);
        ToolDefinition def = new ToolDefinition("A test tool", Collections.emptyList());
        Tool tool = new Tool("test-tool", def, mockClient);

        ToolResult expectedResult = new ToolResult(
            Collections.singletonList(new ToolResult.Content("text", "success")),
            false
        );

        when(mockClient.invokeTool(eq("test-tool"), any(), any()))
            .thenReturn(CompletableFuture.completedFuture(expectedResult));

        ToolResult actualResult = tool.execute(Collections.emptyMap()).join();
        assertNotNull(actualResult);
        assertEquals("success", actualResult.content().get(0).text());
    }

    @Test
    public void testExecuteToolValidationError() {
        McpToolboxClient mockClient = mock(McpToolboxClient.class);
        // Parameter 'param1' is required
        ToolDefinition.Parameter p1 = new ToolDefinition.Parameter(
            "param1", "string", true, "test param", Collections.emptyList()
        );
        ToolDefinition def = new ToolDefinition("A test tool", Collections.singletonList(p1));
        Tool tool = new Tool("test-tool", def, mockClient);

        // Missing 'param1' should throw IllegalArgumentException
        assertThrows(IllegalArgumentException.class, () -> {
            try {
                tool.execute(Collections.emptyMap()).join();
            } catch (Exception e) {
                if (e.getCause() instanceof IllegalArgumentException) {
                    throw (IllegalArgumentException) e.getCause();
                }
                throw e;
            }
        });
    }
}
