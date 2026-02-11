package com.google.cloud.mcp;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.Mockito.mock;

import java.util.Map;
import org.junit.jupiter.api.Test;

public class MockMcpTest {
    @Test
    public void testClientMock() {
        McpToolboxClient client = mock(McpToolboxClient.class);
        assertNotNull(client);
    }
}
