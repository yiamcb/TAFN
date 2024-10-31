def custom_loss(class_weights, asymmetric_weights, regularization_factor):
    class_weights = tf.convert_to_tensor(class_weights, dtype=tf.float32)
    asymmetric_weights = tf.convert_to_tensor(asymmetric_weights, dtype=tf.float32)

    def loss_function(y_true, y_pred):
        # Calculate weighted cross-entropy loss
        weighted_losses = tf.nn.weighted_cross_entropy_with_logits(y_true, y_pred, pos_weight=class_weights)

        # Apply asymmetric loss terms
        asymmetric_losses = tf.where(tf.equal(y_true, 1), asymmetric_weights * weighted_losses, weighted_losses)

        # Total loss
        total_loss = tf.reduce_mean(asymmetric_losses)

        # Regularization term (encouraging smoothness)
        regularization_loss = tf.reduce_mean(tf.abs(y_pred[:, 1:] - y_pred[:, :-1]))

        # Combine losses
        total_loss += regularization_factor * regularization_loss

        return total_loss

    return loss_function