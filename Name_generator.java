public String[] getRandomlyNames(final int characterLength, final int generateSize) {
    HashSet<String> list = new HashSet<String>();
    for (int i = 0; i < generateSize; ++i) {
        String name = null;
        do {
            name = org.apache.commons.lang.RandomStringUtils.randomAlphanumeric(
                    org.apache.commons.lang.math.RandomUtils.nextInt(characterLength - 1) + 1);
        while(list.contains(name));
        list.add(name);
    }
    return list.toArray(new String[]{});
}
