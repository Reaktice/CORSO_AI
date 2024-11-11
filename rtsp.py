import cv2  # Importa OpenCV per l'elaborazione delle immagini
import tensorflow as tf  # Importa TensorFlow per il machine learning
from object_detection.utils import label_map_util  # Importa utilità per la mappa dei label
from object_detection.utils import visualization_utils as vis_util  # Importa utilità per la visualizzazione

# Percorso del modello di rilevamento (cambia questo percorso al tuo modello)
PATH_TO_MODEL = 'path/to/frozen_inference_graph.pb'
# Percorso del file dei label (cambia questo percorso al tuo file di label)
PATH_TO_LABELS = 'path/to/mscoco_label_map.pbtxt'
# URL della telecamera RTSP (cambia questo URL alla tua telecamera RTSP)
RTSP_URL = 'rtsp://admin:PZAVKH@192.168.1.11:554/channel0'

# Carica il modello di rilevamento
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_MODEL, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

# Carica i label
category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)

# Inizializza la telecamera
cap = cv2.VideoCapture(RTSP_URL)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Esegui il rilevamento degli oggetti
    with detection_graph.as_default():
        with tf.compat.v1.Session(graph=detection_graph) as sess:
            image_np = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')

            (boxes, scores, classes, num_detections) = sess.run(
                [boxes, scores, classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})

            # Visualizza i risultati
            vis_util.visualize_boxes_and_labels_on_image_array(
                image_np,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=8)

            # Mostra il frame con le annotazioni
            cv2.imshow('Detected Objects', cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
