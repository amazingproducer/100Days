// still totally borrowing this code

// if you send a push notification from server, it might be instant or delay up 10 minutes
// https://developer.mozilla.org/en-US/docs/Web/API/PushEvent
self.addEventListener('push', function(event) {
  console.log('[Service Worker] Push Received.');
  // push notification can send event.data.json() as well
  console.log(`[Service Worker] Push had this data: "${event.data.text()}"`);

  // https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/showNotification
  const title = 'MyApp Alert';
  const options = {
    body: event.data.text(),
    icon: '/static/img/icon-512.png',
    badge: '/static/img/icon-96.png',
    tag: 'alert'
  };

  event.waitUntil(self.registration.showNotification(title, options));
});


self.addEventListener('notificationclick', function(event) {
  // can handle different type of notification based on event.notification.tag
  console.log(`[Service Worker] Notification click Received: ${event.notification.tag}`);

  event.notification.close();

  // Modify code from https://developer.mozilla.org/en-US/docs/Web/API/WindowClient/focus
  // find existing "/notification" window to focus on, or open a new one if not available
  event.waitUntil(clients.matchAll({
    type: "window"
  }).then(function(clientList) {
    const client = clientList.find(function(c) {
      new URL(c.url).pathname === '/notification'
    });
    if (client !== undefined) {
      return client.focus();
    }

    return clients.openWindow('/notification');
  }));
});

