// still totally borrowing this code

// if you send a push notification from server, it might be instant or delay up 10 minutes
// https://developer.mozilla.org/en-US/docs/Web/API/PushEvent
self.addEventListener('push', function(event) {
  console.log('[Service Worker] Push Received.');
  // push notification can send event.data.json() as well
  console.log(`[Service Worker] Push had this data: "${event.data.text()}"`);

  // https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerRegistration/showNotification
  const title = 'LongJacket Alert';
  const options = {
    body: event.data.text(),
    icon: '/images/e3e8e963-3a4a-7244-cefd-4d6eda8690e4.webPlatform.png',
    badge: '/images/9aaeccf9-8f8c-e950-5b77-d688b74dc457.webPlatform.png',
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
      new URL(c.url).pathname === '/notify'
    });
    if (client !== undefined) {
      return client.focus();
    }

    return clients.openWindow('/');
  }));
});

