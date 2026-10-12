package com.acme;

public final class RegistryGreeting {
    private RegistryGreeting() {}

    public static String message(String name) {
        return "Hello, " + name + ", from a private Ravenstash package.";
    }
}
