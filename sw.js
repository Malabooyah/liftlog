const CACHE_NAME = "liftlog-v1"
const FILES_TO_CACHE = [
    "index.html",
    "manifest.json",
    "icon-192.png",
    "icon-512.png"
];

self.addEventListener("install", (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) =>{
            return cache.addAll(FILES_TO_CACHE);
        })
    );
});

self.addEventListener("fetch", (event) => {
    const url = new URL(event.request.url);

    if (FILES_TO_CACHE.some((file) => url.pathname.endsWith(file))) {
        event.respondsWith(
            caches.match(event.request).then((cached) => {
                return cached || fetch.apply(event.request);
            })
        );
    }
});
